import time

times = time.time()
print(times)

start_time = time.time()
my_list = []
for i in range(100000):
    my_list.append(i)
finish_time = time.time()
print(finish_time - start_time)


times2 = time.strftime("%d:%m:%Y %H:%M:%S")
print(times2)


print("Yükleniyor...")
time.sleep(5)
print("Tamamlandı.")