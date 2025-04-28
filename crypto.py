import psycopg2
import requests 
import json
import json
import time
from bs4 import BeautifulSoup


def linkResponce(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

best_pcs = {}
with open('links.json', 'r') as file:
    best_pcs = json.load(file)

start_time = time.time()
conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1111', port=5432)
cur = conn.cursor()

def search():
    print('Початок')
    # computerLinks = ['https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=3&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000']
    upperPrice = 8000
    computerLinks = [
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}',
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}',
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 

        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 

        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 

        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}', 
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}',
        f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2900&search%5Bfilter_float_price:to%5D={upperPrice}'
    ]
    for link in computerLinks:
        brain(link)

def brain(link):
    soup = linkResponce(link)
    advertisament = soup.find_all('div', class_='css-1g5933j')
    for i in advertisament:
        try:
            advert_url = "https://www.olx.ua" + i.find('a').get('href')
            soup = linkResponce(advert_url)
            description = soup.find('div', class_='css-19duwlz').text
            price = soup.find('h3', class_='css-fqcbii').text
            photo = soup.find('img', class_='css-1bmvjcs').get('src')
            title = soup.find('h4', class_='css-10ofhqw').text.replace("'", "")
            bad_conditions = ['HP', 'Acer', 'Dell','i5-33', 'i7-860', 'i7 860','i7-26', 'i7 26', 'I7 2', 'i7 3', 'I7-3', 'i7-3', 'i7 4', 'i7-4', 'і7 4', 'I7-4', 'I7 4','i5 33', 'i5-23', 'i5 23', 'i5 2', 'i5-44', 'i5 44', 'I5- 4', 'I5 4', 'I5 - 4', 'і5-4', 'FX', 'fx', 'Fx','i5-35', 'i5 35', 'Xeon', 'xeon', 'i5-34', 'i5-3', 'i5 3', 'і5 3', 'I5-3', 'і5-3', 'I5 3', 'I5-2', 'I5 2', 'і5 2', 'і5-2', 'i5 2', 'i5-2', 'i5 4', 'i5-4', 'i3 4', 'i3-3', 'i3-2', 'Athlon', 'ATHLON', 'athlon', 'atlo', 'A8', 'A10', 'A6', 'Phenom', 'phenom', 'XEON', 'xeon', 'Xeon', '2620', 'fujitsu', 'Fujit', 'Lenovo']
                
            if advert_url not in best_pcs:
                if any(bad_word in description for bad_word in bad_conditions) or len(description) < 86 or len(description.replace(' ', '')) > 600:
                    print(advert_url)
                    continue
                else:
                    best_pcs[advert_url] = photo
                    cur.execute("""
                    INSERT INTO person (name, image_url, description, price, title) 
                    VALUES (%s, %s, %s, %s, %s);
                    """, (advert_url, photo, description, price, title))
                    print(f'Пк пройшов перевірку --> {advert_url}')
        except AttributeError as fail: 
            print(fail)
            continue

search()
conn.commit()

cur.close()
conn.close()
print(best_pcs)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Час виконання: {elapsed_time:.2f} секунд")

with open('links.json', 'w') as file:
    json.dump(best_pcs, file, indent=4)



