import random
import requests


def download_image(image_url, path):
    response = requests.get(image_url)
    
    if response.status_code == 200:
        file_extension = image_url.split('.')[-1].lower()

        if file_extension in ['png', 'jpg']:
            with open(path, 'wb') as f:
                f.write(response.content)
            print('Файл успешно скачан и сохранен как ', path)
        else:
            print('Недопустимый формат файла. Разрешены только PNG и JPG.')
    else:
        print('Не удалось скачать файл. Код ошибки:', response.status_code)


if __name__ == "__main__":
    url = input('Введите вашу ссылку: ')
    save_path = f'./images/downloaded_image_{random.randint(0, 223456789)}.png'
    download_image(url, save_path)
