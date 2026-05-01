# Listeler Pratiği


# Alıştırma 1: Listeye erişim
# Anlamı:
#   colors = ["Black", "White", "Blue", "Yellow"]
#   colors[0]   → ilk eleman (indeks 0'dan başlar)
#   colors[-1]  → son eleman
#   len(colors) → eleman sayısını verir

colors = ["Black", "White", "Red"]

len(colors)

print(colors)


# Alıştırma 2: Ekleme ve silme
# Anlamı:
#   fruits = ["apple", "banana", "cherry"]
#   fruits.append("mango")    → sona ekler
#   fruits.insert(0, "kiwi") → başa ekler
#   fruits.remove("banana")  → o değeri siler

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
fruits.insert(0, "kiwi")
fruits.remove("banana")
print(fruits)


# Alıştırma 3: Döngü ile listeleme
# Anlamı:
#   animals = ["cat", "dog", "bird", "fish"]
#   for item in animals: → her elemanı sırayla alır
#   item.upper()         → büyük harfe çevirir

animals = ["duck", "dog", "cat"]
for item in animals:
    item.upper()
print(animals)

# Alıştırma 4: min, max, sum
# Anlamı:
#   numbers = [4, 8, 15, 16, 23, 42]
#   min(numbers) → en küçük değer
#   max(numbers) → en büyük değer
#   sum(numbers) → tüm elemanların toplamı

numbers = [4, 8, 12, 16, 18]

print(min(numbers))


# Bonus: in operatörü
# Anlamı:
#   cities = ["Istanbul", "Ankara", "Izmir", "Bursa"]
#   "Istanbul" in cities → True veya False döner

cities = ["Istanbul", "Amsterdam", "New York"]

"Istanbul" in cities