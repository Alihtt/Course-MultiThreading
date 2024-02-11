from threading import Thread, Semaphore, current_thread
from time import sleep

num = 0
lock = Semaphore(value=2)
"""
When we have limit to shared source we have use Semaphore to apply limit for accessing to shared source
"""


def add():
    global num
    lock.acquire()
    print(current_thread().name)
    sleep(2)
    num += 1
    lock.release()


th1 = Thread(target=add)
th2 = Thread(target=add)
th3 = Thread(target=add)
th4 = Thread(target=add)
th5 = Thread(target=add)
th6 = Thread(target=add)
th7 = Thread(target=add)

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()

print(f'Finished. Your number is {num}')
