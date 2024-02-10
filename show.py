from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name):
    print(f'Starting {name}...')
    sleep(3)
    print(f'Finished {name}.')


# Creating threads instance
th1 = Thread(target=show, args=('One',))
th2 = Thread(target=show, args=('Two',))

# Starting threads
th1.start()
th2.start()

# Waiting until threads are finished
th1.join()
th2.join()

end = perf_counter()
print(round(end - start))
