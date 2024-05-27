from selenium import webdriver
from PIL import Image
from io import BytesIO
import time


def get_website_screenshot(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, height)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    img = Image.open(BytesIO(screenshot))

    return img


if __name__ == '__main__':
    url = input("Введите ссылку на веб-страницу: ")
    my_screenshot = get_website_screenshot(url)

    if my_screenshot:
        my_screenshot.show()
    else:
        print('ERROR')
