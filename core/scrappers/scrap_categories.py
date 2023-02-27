from requests_html import AsyncHTMLSession
from core.parse_func.check_page import check_if_valid
from core.scrappers.load_pages import load_first_page, load_page
import asyncio


#Функция которая проходится по страницам в заданной категории и скачивает страницы с предварительным просмотром карточек
async def load_category_pages(category_link, max_pages=20, once=3):
    url = category_link
    path = 'html_categories'
    num = int(await load_first_page(url, path=path))

    #Если есть пагинация, значит продолжаем парсить дальше, до максимальной заданной
    if num > 1:

        url_pages = [url+f"?page={i}" for i in range(2, max_pages+1)]

        tasks = []

        for index, url in enumerate(url_pages):
            print(url)
            task = asyncio.create_task(load_page(url, path=path))
            tasks.append(task)

            if (len(tasks) == once) or (index == max_pages-2):
                await asyncio.gather(*tasks)
                tasks = []


                check = check_if_valid(path=path)
                if check:
                    continue
                else:
                    print(f'Мы уже собрали все возможные страницы дальше, нет товара')
                    break


async def find_cards_categories():
    pass





async def scrap_category_cards():
    pass