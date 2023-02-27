from requests_html import AsyncHTMLSession
from core.scrappers.load_pages import load_first_page, load_page
import asyncio

async def scrap_category_pages(category_link, max_pages=20, once=4):
    url = category_link
    num = int(await load_first_page(url))


    if num > 1:

        url_pages = [url+f"&page={i}" for i in range(2, max_pages+1)]

        tasks = []

        for index, url in enumerate(url_pages):
            task = asyncio.create_task(load_page(url))
            tasks.append(task)

            if (len(tasks) == once) or (index == max_pages-2):
                session = AsyncHTMLSession()
                await asyncio.gather(*tasks)
                tasks = []
