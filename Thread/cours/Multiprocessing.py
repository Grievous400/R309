import time
import multiprocessing
def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

def ratio():
    print("aa")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p3 =multiprocessing.Process(target=ratio)
    p1.start()
    p2.start()
    p3.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")