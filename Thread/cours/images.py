import time
import concurrent.futures
import requests
img_urls = [
'https://cdn.pixabay.com/photo/2020/01/20/20/20/mallard-4781333_960_720.jpg',
'https://cdn.pixabay.com/photo/2016/03/01/13/42/platypus-1230414_960_720.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]+(".jpg")
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")