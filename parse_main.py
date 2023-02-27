import asyncio

from core.scrappers.scrap_categories import scrap_category_pages

url = 'https://www.wildberries.ru/catalog/detyam/odezhda/dlya-malchikov/bryuki-i-shorty'


async def run_categories():
    await scrap_category_pages(category_link=url,
                               max_pages=15, once=5)


if __name__ == "__main__":
    asyncio.run(run_categories())
