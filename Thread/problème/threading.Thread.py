import concurrent.futures

import requests
import threading

img_urls = [
    'https://cdn.pixabay.com/photo/2020/01/20/20/20/mallard-4781333_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_960_720.jpg'

]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == '__main__':

    t1 = threading.Thread(target=download_image, args=[img_urls[0]])
    t1.start()
    t2 = threading.Thread(target=download_image, args=[img_urls[1]])

    t2.start()

    t1.join()
