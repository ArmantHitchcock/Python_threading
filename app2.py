import concurrent.futures
import time

start = time.perf_counter() #start timer

def doSomething(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'done sleeping..'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(doSomething, 1)
    print(f1.result())
'''
# old way of threading
threads = []

for _ in range(10):
    t = threading.Thread(target=doSomething, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
'''
finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
