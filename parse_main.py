import asyncio
from core.scrappers.scrap_categories import load_category_pages




async def run_categories():
    url = 'https://www.wildberries.ru/catalog/igrushki/dlya-pesochnitsy'
    await load_category_pages(category_link=url, max_pages=4, once=3)


if __name__ == "__main__":
    asyncio.run(run_categories())
