
import requests 
import json
import json
import time
from bs4 import BeautifulSoup


def linkResponce(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

best_pcs = []
with open('links.json', 'r') as file:
    links = json.load(file)

data = []
def search():
    print('Початок')
    # Логіка пошуку компів
    computerLinks = ['https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000']
    # computerLinks = ['https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=3&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&page=3&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=3&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&search%5Bfilter_float_price:from%5D=2000&search%5Bfilter_float_price:to%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=2&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=3&search%5Bfilter_float_price%3Afrom%5D=2000&search%5Bfilter_float_price%3Ato%5D=11000']
    for link in computerLinks:
        print('Початок перевірки силки')

        soup = linkResponce(link)
        advertisament = soup.find_all('div', class_='css-1g5933j')
        for i in advertisament:
            start_time = time.time()
            advert_url = "https://www.olx.ua" + i.find('a').get('href')
            soup = linkResponce(advert_url)
            description = soup.find('div', class_='css-19duwlz').text
            # price = int(float(soup.find('h3', class_='css-fqcbii').text.replace('грн.', '').replace(' ', '').replace('Договірна', '').replace('Договорная', '').replace('/за1шт.', '')))

            bad_conditions = ['HP', 'Acer', 'Dell','i5-33', 'i7-860', 'i7 860','i7-26', 'i7 26', 'I7 2', 'i7 4', 'i7-4', 'i5 33', 'i5-23', 'i5 23', 'i5-44', 'i5 44', 'FX', 'fx','i5-35', 'i5 35', 'Xeon', 'xeon', 'i5-34', 'i5-3', 'i5 3', 'і5 3', 'і5-3', 'I5-2', 'I5 2', 'і5 2', 'і5-2', 'i5 2', 'i5-2', 'i5 4', 'i5-4', 'Athlon', 'A8', 'A10', 'A6']

            if any(bad_word in description for bad_word in bad_conditions) or len(description) < 86:
                continue
            else:
                best_pcs.append(advert_url)
                print(f'Пк пройшов перевірку --> {advert_url}')
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Час виконання: {elapsed_time:.2f} секунд")



search()
print(best_pcs)
with open('links.json', 'w') as file:
    json.dump(links, file, indent=4)



