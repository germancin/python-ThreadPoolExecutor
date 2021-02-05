from concurrent.futures import ThreadPoolExecutor
import time
import random

def wait_function(x, y):
    time.sleep(random.randint(1, 10))
    print(f"Task( {x} multiply {y}, ) completed")
    return x * y

def callback_function(future):
    print('Callback with the following result', future.result())

with ThreadPoolExecutor(max_workers=32) as executor: #change max_workers to 2 and see the results
    future = executor.submit(wait_function, 1, 1)
    future.add_done_callback(callback_function)

    future2 = executor.submit(wait_function, 2, 2)
    future2.add_done_callback(callback_function)

    future3 = executor.submit(wait_function, 3, 3)
    future3.add_done_callback(callback_function)

    start = time.time()
    while True:
        # if(future.running()):
        #     print("Task 1 running")
        # if(future2.running()):
        #     print("Task 2 running")
        # if (future3.running()):
        #     print("Task 3 running")

        if(future.done() and future2.done() and future3.done()):
            print(future.result(), future2.result(), future3.result())
            break
    print(time.time() - start)
