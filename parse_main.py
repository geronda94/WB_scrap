import asyncio
from requests_html import AsyncHTMLSession
import aiofiles
import os
from headers import headers,cookies
from parser_core.load_html import  load_first_page
from parser_core.saving_html import save_html_page


async def print_firs():
    session = AsyncHTMLSession()
    url = 'https://www.wildberries.ru/catalog/igrushki/antistress?sort=popular'
    num = await load_first_page(url, session)

    url_pages = [url+f"&page={i}" for i in range(1,num+1)]
    for i in url_pages:
        print(i)



    await session.close()



if __name__ == "__main__":
    asyncio.run(print_firs())