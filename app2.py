import threading
import time

start = time.perf_counter() #start timer

def doSomething():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('done sleeping..')

t1 = threading.Thread(target=doSomething)
t2 = threading.Thread(target=doSomething)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
