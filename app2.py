import threading
import time

start = time.perf_counter() #start timer

def doSomething():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('done sleeping..')

threads = []

for _ in range(10):
    t = threading.Thread(target=doSomething)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
