from time import sleep, perf_counter
from threading import Thread
import sys

start = perf_counter()


def show(name, delay):
    print(f'Starting {name}...')
    sleep(delay)
    print(f'Finished {name}.')


# Creating threads instance
th1 = Thread(target=show, args=('One', 3), daemon=True)
th2 = Thread(target=show, args=('Two', 7), daemon=True)

# Starting threads
th1.start()
th2.start()

end = perf_counter()
print(round(end - start))

"""
daemon note

if daemon == True:
    print('the thread does not wait for the answer and run sys.exit()')
else:
    print('the thread waits for the answer and after receiving the answer runs sys.exit()')
"""
sys.exit()
