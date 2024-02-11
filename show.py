from threading import Timer


def show():
    print('how u doing buddy?')


t = Timer(10, show)  # Our function will run after 10 seconds
t.start()
