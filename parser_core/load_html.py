from requests_html import AsyncHTMLSession

from parser_core.parse.parsing_html import son_page_html
from parser_core.saving_html import save_html_page


async def load_page(url, index):
    session = AsyncHTMLSession()
    flag = False
    path_to_save = 'html_main'
    index= url.split('page_')[-1].split('.html')[0]



    try:
        response = await session.get(url)
        print('Начинаю рендеринг страницы №', index)

        await response.html.arender(sleep=0.5, keep_page=True, scrolldown=30)
        html_content = response.html.html


        await save_html_page(html_content, index, path_to_save=path_to_save)
        flag = True



    finally:
        print(f'Прошелся по странице {index}, результат: ',flag)





async def load_first_page(url):
    session = AsyncHTMLSession()
    flag = False
    path_to_save = 'html_main'
    index =1
    son_page = 0

    try:
        response = await session.get(url)
        print('Начинаю рендеринг страницы №', index)

        await response.html.arender(sleep=0.5, keep_page=True, scrolldown=30)
        html_content = response.html.html


        son_page = await son_page_html(html_content)
        await save_html_page(html_content, index, path_to_save=path_to_save)
        flag = True



    finally:
        print(f'Прошелся по главной странице, результат: ',flag)

        return son_page










if __name__ == "__main__":
    print("Этот файл не предназначен для прямого запуска!")