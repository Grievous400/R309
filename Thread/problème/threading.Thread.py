import time
import concurrent.futures
import requests
import threading

img_urls = [
    'https://cdn.pixabay.com/photo/2020/01/20/20/20/mallard-4781333_960_720.jpg',
    'https://cdn.pixabay.com/photo/2016/03/01/13/42/platypus-1230414_960_720.jpg'
]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4] + (".jpg")
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == '__main__':
    t1 = threading.Thread(target=download_image, args=[img_urls])
    t1.start()
    t1.join()