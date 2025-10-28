# For and While

numbers = [1,2,3,4,5,6,7,8]

for i in numbers:
    print(i)

print("")

for i2 in range(1, 19, 2): # başlangıç dahil başlat, son değer dahil değile kadar, aralık değeri
    print(i2)

print("")

letter_list = ["a", "b", "c", "d"]
number_list = [1, 2, 3, 4]

for l in letter_list:
    for n in number_list:
        print(l, n)

print("")

number_list2 = [1,2,3,4,5,6,7,8,9]

for i3 in number_list2:
    if i3 == 3:
        continue # break -> 3 dahil sonrasını ekrana yazma
    print(i3)

print("")

example_list = range(100)

for i4 in example_list:
    if i4 % 3 != 0:
        continue
    if i4 == 93: # 93 dahil sonrasını dahil etme
        break
    print(i4)

print("")

# yukarıdaki örneğin daha kolayı
x = 4

while x <= 40:
    print(x)
    x += 4

print("")

y = 1

while True: # 1'den 100'e kadar yazdır
    print(y)
    y += 1
    if y == 120:
        break

print("")

while True: # Sonsuz döngü
    print(y)
    y += 1