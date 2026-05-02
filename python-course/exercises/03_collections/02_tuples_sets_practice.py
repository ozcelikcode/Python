# Tuple ve Set Pratiği


# Alıştırma 1: Tuple oluşturma ve erişim
# Anlamı:
#   coordinates = (10, 20, 30)  → tuple, değiştirilemez liste gibidir
#   coordinates[0]              → ilk elemana erişir
#   len(coordinates)            → eleman sayısını verir

coordinates = (10, 20, 30)

print(coordinates[1])


# Alıştırma 2: Tuple değiştirilemez
# Anlamı:
#   point = (5, 10)
#   point[0] = 99   → hata verir! tuple'lar değiştirilemez
#   point           → sadece okuyabilirsin

point = (5, 10)
# point[0] = 40 # hata
print(point)


# Alıştırma 3: Set oluşturma
# Anlamı:
#   unique_numbers = {1, 2, 3, 3, 2, 1}  → tekrar eden değerleri atar
#   print(unique_numbers)                 → {1, 2, 3} görünür

unique_numbers = {1, 2, 3, 4, 4, 3, 2, 1, 0}
print(unique_numbers)



# Alıştırma 4: Set metodları
# Anlamı:
#   tags = {"python", "code", "learning"}
#   tags.add("practice")    → eleman ekler
#   tags.remove("code")     → eleman siler
#   print(tags)             → güncel hali gösterir

language = "JavaScript"
other_language = "C++"
other = "code"

tags = {"Python", "Java", "Swift", other}
tags.add(language + " and " + other_language)
tags.remove(other)

print(tags)

# Alıştırma 5: İki set arasındaki işlemler
# Anlamı:
#   a = {1, 2, 3, 4}
#   b = {3, 4, 5, 6}
#   a & b   → ikisinde de olanlar (kesişim): {3, 4}
#   a | b   → hepsini birleştirir (birleşim): {1, 2, 3, 4, 5, 6}
#   a - b   → sadece a'da olanlar: {1, 2}


a = {1, 50, 100, 150, 200}
b = {2, 75, 125, 175, 225}

print(a & b) # set() yazar. kesişim yoktur
print(a | b)
print(a - b)
print(a ^ b)