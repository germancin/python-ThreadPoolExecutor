from concurrent.futures import ThreadPoolExecutor
import time
import os
import random

def fibo(n):
    a = 0
    b = 1
    total_sum = 0
    count = 1
    # print("Fibonacci Series: ", end=" ")
    while count <= n:
        # print(total_sum, end=" ")
        count += 1
        a = b
        b = total_sum
        total_sum = a + b

    return total_sum

def wait_function(position):
    start = time.time()
    n = random.randint(99999, 999999)
    total_sum = fibo(n)
    # time.sleep(random.randint(1, 5))
    print(f"Fibo de: {n} ::::Execution time: {time.time() - start}   completed {position}")
    return total_sum

def callback_function(future):
    # print('Callback with the following result', future.result())
    print('Callback with the following result')

with ThreadPoolExecutor(max_workers=32) as executor: #change max_workers to 2 and see the results
    future = executor.submit(wait_function, 'first')
    future.add_done_callback(callback_function)
    future2 = executor.submit(wait_function, 'second')
    future2.add_done_callback(callback_function)

    start = time.time()
    while True:
        if(future.done() and future2.done()):
            # print(future.result(), future2.result())
            break
    print(time.time() - start)