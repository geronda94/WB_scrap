import asyncio
from requests_html import AsyncHTMLSession
import aiofiles
import os
from headers import headers,cookies
from parser_core.load_html import  load_first_page
from parser_core.saving_html import save_html_page


async def print_firs():

    url = 'https://www.wildberries.ru/catalog/igrushki/antistress?sort=popular'
    num = await load_first_page(url)


    if num > 1:
        url_pages = [url+f"&page={i}" for i in range(1,num+1)]

        tasks = []

        for index, url in enumerate(url_pages):
            task = asyncio.create_task(save_html_page(url, index))
            tasks.append(task)
        await asyncio.gather(*tasks)







if __name__ == "__main__":
    asyncio.run(print_firs())