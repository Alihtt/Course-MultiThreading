from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name, delay):
    print(f'Starting {name}...')
    sleep(delay)
    print(f'Finished {name}.')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


# Creating threads instance
th1 = ShowThread('One', 3)
th2 = ShowThread('Two', 7)

# Starting threads
th1.start()
th2.start()

# Waiting until threads are finished
th1.join()
th2.join()

end = perf_counter()
print(round(end - start))
