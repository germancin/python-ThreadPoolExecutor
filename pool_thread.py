from concurrent.futures import ThreadPoolExecutor
import threading
import random
import multiprocessing


def task(n):
    print(f"Processing {format(n)}")


def main():
    executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count()):
        task_exe = executor.submit(task)
        print(f'Task# {i}')

    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        for i in range(multiprocessing.cpu_count()):
            future = executor.submit(task, (2))
            future = executor.submit(task, (3))
            future = executor.submit(task, (4))


if __name__ == '__main__':
    main()
