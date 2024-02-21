import re
import requests
from requests.exceptions import MissingSchema
import socket


def check_site(adress, domen):
    site = f'https://www.{adress}{domen}'
    try:
        response = requests.get(site)
        print(f'На сайт "{site}" можно перейти')
        check_ip(adress, domen)
        number = find_number(response)
        if check_number(number):
            print('Номер корректный')
        else:
            print('Номер не корректный')
    except MissingSchema :
        print(f'Сайт "{site}" не открывается')


def check_number(number):
    if type(number) == str:
        test_1 = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', number)
        test_2 = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{4}\)?[\- ]?)?[\d\- ]{7,10}$', number)
        test_3 = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{5}\)?[\- ]?)?[\d\- ]{7,10}$', number)
        return bool(test_1) or bool(test_2) or bool(test_3)
    else:
        return False



def check_ip(adress, domen):
    print('IP адрес сайта: ', socket.gethostbyname(f'{adress}{domen}'))


def find_number(response):
    string_with_number = ''
    for item in response:
        if b'phone-number' in item:
            string_with_number = item.decode()
    if string_with_number != '':
        left_index = string_with_number.find('white">')
        right_index = string_with_number.find('</a>')
        return string_with_number[left_index+len('white">'):right_index]
    else:
        return 'Номер не найден'


if __name__ == '__main__':
    adress = 'sstmk'
    domen = '.ru'
    check_site(adress, domen)