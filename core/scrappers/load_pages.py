from requests_html import AsyncHTMLSession
from core.parse_func.parsing_pagination import son_page_html
from core.saving_html import save_html_page
from headers import cookies,headers
import aiohttp

async def load_page(url, path):
    global html_content
    session = AsyncHTMLSession()

    flag = False
    path_to_save = path
    index = url.split('page=')[-1].split('.html')[0]



    try:
        response = await session.get(url)
        print('Начинаю рендеринг страницы №', index)

        await response.html.arender(sleep=0.5, keep_page=True, scrolldown=30)
        html_content = response.html.html

        await save_html_page(html_content, index, path_to_save=path_to_save)
        flag = True



    finally:
        await session.close()
        print(f'Прошелся по странице {index}, результат: ',flag)
        chek_validation = 'Мы уже делаем все возможное, чтобы это исправить. Попробуйте повторить попытку позднее. А пока вы можете продолжить выбирать товары.'
        return chek_validation not in str(html_content)






async def load_first_page(url, path):
    global html_content
    session = AsyncHTMLSession()
    session.proxies  = {}

    flag = False
    path_to_save = path
    index =1


    try:
        response = await session.get(url)
        print('Начинаю рендеринг страницы №', index)

        await response.html.arender(sleep=0.5, keep_page=True, scrolldown=30)
        html_content = response.html.html

        await save_html_page(html_content, index, path_to_save=path_to_save)
        flag = True



    finally:
        await session.close()
        print(f'Прошелся по странице {index}, результат: ', flag)
        chek_validation = 'Мы уже делаем все возможное, чтобы это исправить. Попробуйте повторить попытку позднее. А пока вы можете продолжить выбирать товары.'
        return chek_validation not in str(html_content)










if __name__ == "__main__":
    print("Этот файл не предназначен для прямого запуска!")