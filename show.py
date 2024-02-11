from threading import Thread, Event
from time import sleep


def first(f, s):
    sleep(10)
    print('First is ready ... ')
    f.set()
    s.wait()
    print('First is working ... ')
    f.clear()


def second(f, s):
    print('Second is ready ... ')
    s.set()
    f.wait()
    print('Second is working ... ')
    s.clear()


"""
This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.

https://docs.python.org/3/library/threading.html#event-objects
"""

f = Event()
s = Event()

th1 = Thread(target=first, args=(f, s))
th2 = Thread(target=second, args=(f, s))

th1.start()
th2.start()
