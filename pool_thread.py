from concurrent.futures import ThreadPoolExecutor
import threading
import random
import multiprocessing


def task(n):
    print(f"Processing {format(n)}")


def main():
    executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        i = 1
        for i in range(multiprocessing.cpu_count()):
            task_exe = executor.submit(task (random.randint(1,4)))


if __name__ == '__main__':
    main()
