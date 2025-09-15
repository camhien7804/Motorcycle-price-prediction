import requests
from bs4 import BeautifulSoup
import csv
import time
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def check_none(info):
    if info:
        return info.text.replace(" ", "")
    return "Null"

def scrape_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    try:
        response = session.get(url, headers=headers, timeout=10)
        print(f"Status code for {url}: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        listings = soup.find_all('a', class_='cebeqpz')
        print(f"Found {len(listings)} listings on this page")
        
        if not listings:
            print("No listings found on this page. Adding empty row.")
            return [{}]
        
        data = []
        for listing in listings:
            bwq0cbs_elems = listing.find_all('span', class_='bwq0cbs')
            motor_type = check_none(bwq0cbs_elems[1] if len(bwq0cbs_elems) > 1 else None)
            condition = check_none(bwq0cbs_elems[2] if len(bwq0cbs_elems) > 2 else None)
            
            price_elem = listing.find('span', class_='bfe6oav')
            price = check_none(price_elem)
            
            href = listing.get('href', None)
            detail_url = f"https://xe.chotot.com{href}" if href else None
            
            brand = reg_year = motor_cap = motor_model = km_nums = "Null"
            
            if detail_url:
                try:
                    detail_response = session.get(detail_url, headers=headers, timeout=10)
                    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
                    
                    detail_divs = detail_soup.find_all('div', class_='pqp26ip')
                    for div in detail_divs:
                        spans = div.find_all('span', class_='bwq0cbs')
                        if len(spans) < 2:
                            continue
                        label = spans[0].text.strip()
                        value = spans[1]
                        
                        if 'Hãng xe:' in label:
                            brand = check_none(value)
                        elif 'Năm đăng ký:' in label:
                            reg_year = check_none(value)
                        elif 'Tình trạng xe:' in label:
                            condition = check_none(value)
                        elif 'Dung tích xe:' in label:
                            motor_cap = check_none(value)
                        elif 'Dòng xe:' in label:
                            motor_model = check_none(value)
                        elif 'Số Km đã đi:' in label:
                            km_nums = check_none(value)
                        elif 'Loại xe:' in label:
                            motor_type = check_none(value)
                    
                    print(f"Detail page {detail_url}: Brand={brand}, Reg Year={reg_year}, Condition={condition}, Capacity={motor_cap}, Model={motor_model}, Mileage={km_nums}, Type={motor_type}, Price={price}")
                except requests.RequestException as e:
                    print(f"Error fetching detail page {detail_url}: {e}")
            
            data.append({
                'Brand': brand,
                'Registration Year': reg_year,
                'Condition': condition,
                'Capacity': motor_cap,
                'Model': motor_model,
                'Mileage': km_nums,
                'Type of Motorcycle': motor_type,
                'Price': price,              
            })
        
        return data
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return [{}]

def main():
    base_url = 'https://xe.chotot.com/mua-ban-xe-may?page={}'
    all_data = []
    max_pages = 1000
    
    with open('moto_crawl.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Brand', 'Registration Year', 'Condition', 'Capacity', 'Model', 'Mileage', 'Type of Motorcycle', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        try:
            for page in range(1, max_pages + 1):
                print(f"Scraping page {page}...")
                url = base_url.format(page)
                page_data = scrape_page(url)
                
                all_data.extend(page_data)
                for item in page_data:
                    writer.writerow(item)
                
                csvfile.flush()
                
                print(f"Total listings scraped so far: {len([d for d in all_data if d.get('Type of Motorcycle') != 'Null'])} (excluding empty rows)")
                
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\nStopped by user. Saving data...")
            pass
    
    print(f"Scraped {len([d for d in all_data if d.get('Type of Motorcycle') != 'Null'])} listings successfully (excluding empty rows). Data saved to moto_crawl.csv")

if __name__ == '__main__':
    main()