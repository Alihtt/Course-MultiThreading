from threading import Thread, Lock

num = 0
lock = Lock()
"""
If we are working on one source in multiple functions like {num} in add and subtract 
it can be race condition and return nonsense answer, for avoiding that our program need to be thread safe
we have to use lock in each function to lock the thread and after finishing thread next function will be start in other hand respect each other
"""


def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


th1 = Thread(target=add)
th2 = Thread(target=subtract)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Finished. Your number is {num}')
