import pandas as pd
import requests 
import json
import numpy
from threading import Thread
import json
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from email.message import EmailMessage
from sklearn.model_selection import train_test_split


def linkResponce(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

illa = 0
print(illa)

def get_Date(product):
    prices = []
    soup1 = linkResponce(f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/q-{product}/?currency=UAH&search%5Bprivate_business%5D=private&search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_subcategory%5D%5B0%5D=videokarty')
    advertisament = soup1.find_all('div', class_='css-1g5933j')
    for i in advertisament:
        advert_url = "https://www.olx.ua" + i.find('a').get('href')
        ogoloshenna = linkResponce(advert_url)
        if product.lower().replace('-', ' ') in ogoloshenna.find('h4', class_='css-yde3oc').text.lower(): prices.append(int(float(ogoloshenna.find('h3', class_='css-fqcbii').text.replace('грн.', '').replace(' ', '').replace('Договірна', '').replace('Договорная', '').replace('/за1шт.', ''))))

    mean = numpy.mean(prices) #Знаходить середнє значення
    std_dev = numpy.std(prices) #Знаходить стандартне відхилення він середньої ціни
    average_price = [p for p in prices if mean - 2*std_dev <= p <= mean + 2*std_dev]
    return numpy.mean(average_price)

# def main():
#     type_ = input('Processor or VideoCard?: 1/2')
#     if type_ == '1': type_ = 'protsessory'
#     else: type_ = 'videokarty'
#     product = input('Name product: ')
#     print(get_Date(linkResponce(f'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/q-{product}/?currency=UAH&search%5Bfilter_enum_subcategory%5D%5B0%5D={type_}'), product))

best_pcs = []
with open('links.json', 'r') as file:
    links = json.load(file)


data = []
def search():
    print('Початок')
    # Логіка пошуку компів
    computerLinks = ['https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=1&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BF%D0%BA/?currency=UAH&page=3&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&page=1&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&page=2&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BF%D0%BA/?currency=UAH&page=3&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=1&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=2&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/if/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=3&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=1&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=2&search%5Bfilter_float_price%3Ato%5D=11000', 'https://www.olx.ua/uk/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/q-%D1%96%D0%B3%D1%80%D0%BE%D0%B2%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8E%D1%82%D0%B5%D1%80/?currency=UAH&page=3&search%5Bfilter_float_price%3Ato%5D=11000']
    for link in computerLinks:
        print('Початок перевірки силки')
        try:
            soup = linkResponce(link)
            advertisament = soup.find_all('div', class_='css-1g5933j')
            for i in advertisament:
                advert_url = "https://www.olx.ua" + i.find('a').get('href')
                global illa
                illa = illa + 1
                print(illa)
                soup = linkResponce(advert_url)
                description = soup.find('div', class_='css-19duwlz').text
                price = int(float(soup.find('h3', class_='css-fqcbii').text.replace('грн.', '').replace(' ', '').replace('Договірна', '').replace('Договорная', '').replace('/за1шт.', '')))

                print(67)
                brain(description, price, advert_url)
        except:
            continue

def brain(desc, price, link):
    desc = desc.lower()
    print('Перевірка пк')

    processor_keywords = {'i3', 'i5', 'i7', 'xeon', 'intel', 'athlon', 'fx', 'pentium', 'ryzen'}
    videocard_keywords = {'gtx', 'rx', '1060', '580', '470', '570', '1050', '1070', 'rtx'}

    for p in processor_keywords:
        if p in desc: 
            processor = p
            break
        else:
            processor = None
    
    for v in videocard_keywords:
        if v in desc:
            videocard = v
            break
        else:
            videocard = None

    flag = False
    if processor:
        ryzen_processors = ['3 120', '3 130', '5 140', '5 150', '5 160', '7 170', '7 180', '3 220', '5 240', '5 260', '7 270', '7 280', '3 310', '3 330', '5 350', '5 360', '7 370', '9 390', '3 430', '5 450', '7 470', '9 490', '5 560', '7 570', '9 590', '9 595', '3 410', '3 430', '5 450', '5 460', '7 470', '3 510', '3 530', '5 550', '5 560', '5 570', '7 570', '7 580', '7 590', '9 590', '9 595', '5 760', '5 770', '7 770', '7 780', '9 790', '9 795']
        processor_map = {'610': 'i3-6100', '347': 'i5-3470', '240': 'i5-2400', '377': 'i7-3770','pent': 'Pentium', '357': 'i5-3570', '467': 'i5-4670', '446': 'i5-4460','phe': 'Phenom', '260': 'i7-2600', 'athl': 'athlon', 'pen': 'Pentium','xeon': 'Xeon', '1010': 'i3-10100', 'a8': 'Athlon A8', '104': 'i5-10400','fx': 'FX', '650': 'i5-6500', '860': 'i5-8600', '940': 'i5-9400','640': 'i5-6400', '457': 'i5-4570', '750': 'i5-7500', '740': 'i5-7400','710': 'i3-7100', '910': 'i3-9100', '660': 'i7-6700', '870': 'i7-8700','840': 'i5-8400', '830': 'i3-8300', '960': 'i7-9700', '990': 'i9-9900','107': 'i7-10700', '109': 'i9-10900'}
        index = desc.find(processor)
        if index != -1:
            if processor == 'ryzen':
                processor = desc[index:index + 12]
                for proc in ryzen_processors:
                    if proc in processor:
                        processor = proc
                        processor = 'Ryzen ' + processor + '0'
                        flag = True
                        break
            else:
                processor = desc[index:index + 7]
                for key, value in processor_map.items():
                    if key in processor:
                        processor = value
                        flag = True
                        break
    else:
        print("Невизначений процесор", link)
        links[link] = 'True'
        return False

    if flag == False or processor == None:
        links[link] = 'True'
        print('Силка', link)
        return False

    if videocard:
        videocard_map = {'105': 'GTX 1050 TI', '106': 'GTX 1060', '580': 'RX 580', '950': 'GTX 950','470': 'RX 470', '570': 'RX 570', '165': 'GTX 1650', '166': 'GTX 1660','107': 'GTX 1070', '940': 'GT 940M', '960': 'GTX 960', '970': 'GTX 970','980': 'GTX 980', '980 ti': 'GTX 980 TI', '750': 'GTX 750', '750 ti': 'GTX 750 TI','760': 'GTX 760', '770': 'GTX 770', '780': 'GTX 780', '780 ti': 'GTX 780 TI', '7750': 'HD 7750', '7770': 'HD 7770', '7850': 'HD 7850','7870': 'HD 7870', '7950': 'HD 7950', '7970': 'HD 7970', 'r9 270': 'R9 270','r9 280': 'R9 280', 'r9 290': 'R9 290', 'r9 290x': 'R9 290X', 'r9 380': 'R9 380','r9 390': 'R9 390', 'r9 390x': 'R9 390X', 'r7 240': 'R7 240', 'r7 250': 'R7 250','r7 260': 'R7 260', 'r7 265': 'R7 265', 'intel hd': 'Intel HD Graphics','uhd': 'Intel UHD Graphics', 'gt 1030': 'GT 1030', 'gt 730': 'GT 730','gt 710': 'GT 710'}
        index = desc.find(videocard)
        if index != -1:
            videocard = desc[index:index + 7]
        
        for key, value in videocard_map.items():
            if key in videocard:
                videocard = value
                break
    
    data.append((videocard, processor, price))



def create_excel(data, filename="computer_prices.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "PC Prices"

    # Заголовки
    ws.append(["GPU", "CPU", "Price (UAH)"])

    # Додаємо всі рядки з даними
    for gpu, cpu, price in data:
        ws.append([gpu, cpu, price])

    # Зберігаємо файл
    wb.save(filename)
    print(f"Excel-файл '{filename}' створено.")
    return filename


def send_email(receiver_email, filename):
    sender_email = "sakovskiy3.0@gmail.com" 
    sender_password = "xsok qshw konu nden"  
    msg = EmailMessage()
    msg["Subject"] = "Файл Excel із цінами комп'ютерів"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Ось ваш список комп'ютерних збірок у форматі Excel.")

    # Додаємо Excel-файл
    with open(filename, "rb") as file:
        msg.add_attachment(file.read(), maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=filename)

    # Відправка через SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print(f"Лист із файлом '{filename}' надіслано на {receiver_email}")


    




search()
receiver_email = "sakovskiy3.0@gmail.com"
excel_file = create_excel(data)
send_email(receiver_email, excel_file)


with open('./test/links.json', 'w') as file:
    json.dump(links, file, indent=4)

with open('DataBase.json', 'w') as file:
    json.dump(best_pcs, file, indent=4)
    print('All good')


