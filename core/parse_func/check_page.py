from bs4 import BeautifulSoup
import asyncio
import os

def check_if_valid(path):
    path = os.listdir(path)[1]
    print(path)
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html = file.read()

    except:
        return False

    soup = BeautifulSoup(html, 'lxml')

    class_error = soup.find('div', class_='error500__container')
    if class_error:
        return False
    else:
        return True


def runi():
    ret = check_if_valid(path='../../html_categories')
    print(ret)




#asyncio.run(runi())