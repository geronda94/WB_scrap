import asyncio
from requests_html import AsyncHTMLSession
import aiofiles
import os
from headers import headers,cookies
from parser_core.scrap_functions import parse_first_page
from parser_core.saving_html import save_html_page


async def print_firs():
    session = AsyncHTMLSession()

    await parse_first_page('https://www.wildberries.ru/catalog/igrushki/antistress?sort=popular&pag',1, session)

    await session.close()



if __name__ == "__main__":
    asyncio.run(print_firs())