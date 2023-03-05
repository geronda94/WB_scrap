import os

def check_if_valid(path):
    path_file = os.listdir(path)[-1]
    path_dir = path
    try:
        with open(f'{path_dir}/{path_file}', 'r', encoding='utf-8') as file:
            html = file.read()
    except Exception as ex:
        print('Ошибка открытия файла ', ex)
        print(path)



    chek_text ='Мы уже делаем все возможное, чтобы это исправить. Попробуйте повторить попытку позднее. А пока вы можете продолжить выбирать товары.'


    if chek_text in html:
        return False
    else:
        return True


def runi():
    ret = check_if_valid(path='../../html_categories')
    print(ret)



