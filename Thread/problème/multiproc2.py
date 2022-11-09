import multiprocessing
import requests
img_urls = [
    'https://cdn.pixabay.com/photo/2016/01/05/17/51/maltese-1123016_960_720.jpg',
    'https://cdn.pixabay.com/photo/2016/07/15/15/55/dachshund-1519374_960_720.jpg'

]
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=download_image, args=[img_urls[0]])
    p2 = multiprocessing.Process(target=download_image, args=[img_urls[1]])
    p1.start()
    p2.start()