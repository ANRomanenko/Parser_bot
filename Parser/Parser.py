import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def collect_data(city_code='506'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'active_city_id': f'{city_code}'
    }

    # response = requests.get(url='https://comfy.ua/smartfon/brand__apple/', headers=headers, cookies=cookies)
    #
    # with open(f'index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)

    with open('index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    city = soup.find()

def main():
    collect_data(city_code='506')


if __name__ == '__main__':
    main()