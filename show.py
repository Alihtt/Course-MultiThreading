from threading import Thread, RLock

num = 0
lock = RLock()
"""
If our program is reentrant we need to use RLock to acquired multiple times by the same thread 
"""


def add():
    global num
    with lock:
        subtract()
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


def both():
    subtract()
    add()


th1 = Thread(target=both)

th1.start()

th1.join()

print(f'Finished. Your number is {num}')
