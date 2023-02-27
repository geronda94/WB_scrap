from requests_html import AsyncHTMLSession
from parser_core.saving_html import save_html_page


async def parse_first_page(url, index,session: AsyncHTMLSession()):
    session = session
    flag = False


    try:
        response = await session.get(url)
        print('Начинаю рендеринг страницы №', index)

        await response.html.arender(sleep=0.5, keep_page=True, scrolldown=30)
        html_content = response.html.html

        await save_html_page(html_content, index)
        flag = True



    finally:
        print(f'Прошелся по странице {index}, результат: ',flag)
