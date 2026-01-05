import time

times = time.time()
print(times)

start = time.time()
list = []
for i in range(10):
    list.append(i)
finish = time.time()
print(finish - start)