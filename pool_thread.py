from concurrent.futures import ThreadPoolExecutor
import threading
import random
import multiprocessing


def task():
    print("Executing our Task")
    result = 0
    i = 0
    for i in range(10):
        result = result + i
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))

def main():
    executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count()):
       task_exe = executor.submit(task)
       # print(task_exe)

if __name__ == '__main__':
    main()
