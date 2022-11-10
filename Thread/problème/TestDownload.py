import concurrent.futures
import time
import requests
import threading
import multiprocessing
import sys
img_urls = [
    'https://cdn.pixabay.com/photo/2020/01/20/20/20/mallard-4781333_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_960_720.jpg',
    'https://cdn.pixabay.com/photo/2015/10/30/20/13/sunrise-1014712_960_720.jpg'
]
try:
    y = sys.argv[1]
    a = int(y[5:1024])

except(ValueError):
    print("Ce n'est pas une valeur entière")


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


try:
    y = sys.argv[1]
    a = int(y[5:1024])

except(ValueError):
    print("Ce n'est pas une valeur entière")
else:
    if __name__ == '__main__':
        for i in range(a):
            start1 = time.perf_counter()

            for i in range(len(img_urls)):
                ti = threading.Thread(target=download_image, args=[img_urls[i]])

                ti.start()
                ti.join()
            end1 = time.perf_counter()
            print(f"thread {round(end1 - start1, 2)} second(s)")



            start2 = time.perf_counter()


            for i in range(len(img_urls)):

                pi=multiprocessing.Process(target=download_image, args=[img_urls[i]])
                pi.start()
            end2 = time.perf_counter()
            print(f"processing {round(end2 - start2, 2)} second(s)")



            start3 = time.perf_counter()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(download_image, img_urls)
            end3 = time.perf_counter()
            print(f"pool {round(end3 - start3, 2)} second(s)")
