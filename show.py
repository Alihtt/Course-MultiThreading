from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate

start = perf_counter()


def show(name, delay):
    print(f'Starting {name}...')

    print(current_thread())  # Return the current thread
    print(enumerate())  # Return all alive threads
    
    sleep(delay)
    print(f'Finished {name}.')


# Creating threads instance
th1 = Thread(name='First', target=show, args=('One', 3))
th2 = Thread(name='Second', target=show, args=('Two', 7))

# Starting threads
th1.start()
th2.start()

# Waiting until threads are finished
th1.join()
th2.join()

end = perf_counter()
print(round(end - start))
