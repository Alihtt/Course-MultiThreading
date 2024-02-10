from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

start = perf_counter()


def show(name):
    print(f'Starting {name}...')
    sleep(3)
    print(f'Finished {name}.')


# For large amount of threads we use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    executor.map(show, names)

end = perf_counter()
print(round(end - start))
