import aiofiles
import os




path_to_save = 'html_main'

if not os.path.exists(path_to_save ):
    os.mkdir(path_to_save )


async def save_html_page(html_content, index):
    filename = f"page_{index}.html"
    async with aiofiles.open(f'{path_to_save}/{filename}', "w", encoding="utf-8") as file:
        await file.write(html_content)


