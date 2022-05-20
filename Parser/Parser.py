import datetime
import requests
import csv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def collect_data(city_code='506'): # Принимает параметер код города!
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M') # День, месяц, год, и часы с минутами
    ua = UserAgent() # Объект класса

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'active_city_id': f'{city_code}'
    }

    response = requests.get(url='https://comfy.ua/smartfon/brand__apple/', headers=headers, cookies=cookies)
    #
    # with open(f'index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)

    # with open('index.html', encoding='utf-8') as file:
    #     src = file.read()

    soup = BeautifulSoup(response.text, 'lxml')

    city = soup.find('span', class_='header-top__city-name icon-comfy header-top__more-icon').get_text(strip=True)
    cards = soup.find_all('div', class_='products-list-item products-catalog-grid__item products-list-item--grid')
    # print(city, len(cards))

    with open(f'{city}_{cur_time}.csv', 'w', encoding='utf-32') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(
            (
                'Продукт',
                'Старая цена',
                'Новая цена',
                'Процент скидки'
            )
        )

    for card in cards:
        card_title = card.find('a', class_='products-list-item__name').get_text(strip=True)

        try:
            card_discount = card.find('span', class_='products-list-item__actions-price-discount').get_text(strip=True)
        except AttributeError:
            continue

        price_old = card.find('div', class_='products-list-item__actions-price-old').get_text(strip=True) # Старая цена
        price_current = card.find('div', class_='products-list-item__actions-price-current').get_text(strip=True).replace('₴', '') # Новая цена

        # description = card.find('div', class_='list-item__specifications-text').get_text(strip=True).replace('iPhone 13', ' ').replace('• 09.2021', ' ').replace('• Модель з лінійки ', ' ').strip()

        # print(price_current)

        with open(f'{city}_{cur_time}.csv', 'a', encoding='utf-32') as file:
            writer = csv.writer(file, delimiter=';')

            writer.writerow(
                (
                    card_title,
                    price_old,
                    price_current,
                    card_discount
                )
            )

    print(f'Файл {city}_{cur_time}.csv успешно записан!')

def main():
    collect_data(city_code='506')


if __name__ == '__main__':
    main()