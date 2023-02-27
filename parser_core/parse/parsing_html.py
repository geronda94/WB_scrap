import lxml
from bs4 import BeautifulSoup
import aiofiles
import asyncio


#Обычная функция на поиск последней странциы через код напрямую
def son_page_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    find_pages = soup.find('div', class_="pageToInsert pagination__wrapper").find_all('a',
                                                                                      class_='pagination-item pagination__item j-page')
    son_page = max(int(i.text) for i in find_pages)

    return son_page


#Асинхронная функция на поиск последней странциы через код напрямую
async def son_page_html(html):
    soup = BeautifulSoup(html, 'lxml')
    find_pages = soup.find('div', class_="pageToInsert pagination__wrapper").find_all('a',
                                                                                      class_='pagination-item pagination__item j-page')
    son_page = max(int(i.text) for i in find_pages)

    return son_page

#Обычная функция на поиск последней странциы открытием сохраненной страницы
def son_page(path='../html_main/page_1.html'):
    with open(path, 'r', encoding='utf-8') as file:
        html= file.read()

    soup = BeautifulSoup(html, 'lxml')
    find_pages = soup.find('div', class_="pageToInsert pagination__wrapper").find_all('a', class_='pagination-item pagination__item j-page')
    son_page = max(int(i.text) for i in find_pages)

    return son_page


#Асинхронная функция на поиск последней странциы открытием сохраненной страницы
async def find_son_page(path='../html_main/page_1.html'):
    async with aiofiles.open(path, 'r', encoding='utf-8') as file:
        html = await file.read()

    soup = BeautifulSoup(html, 'lxml')
    find_pages = soup.find('div', class_="pageToInsert pagination__wrapper").find_all('a', class_='pagination-item pagination__item j-page')
    son_page = max(int(i.text) for i in find_pages)

    return son_page

