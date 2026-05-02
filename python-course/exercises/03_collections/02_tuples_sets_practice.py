# Tuple ve Set Pratiği


# Alıştırma 1: Tuple oluşturma ve erişim
# Anlamı:
#   coordinates = (10, 20, 30)  → tuple, değiştirilemez liste gibidir
#   coordinates[0]              → ilk elemana erişir
#   len(coordinates)            → eleman sayısını verir


# Alıştırma 2: Tuple değiştirilemez
# Anlamı:
#   point = (5, 10)
#   point[0] = 99   → hata verir! tuple'lar değiştirilemez
#   point           → sadece okuyabilirsin


# Alıştırma 3: Set oluşturma
# Anlamı:
#   unique_numbers = {1, 2, 3, 3, 2, 1}  → tekrar eden değerleri atar
#   print(unique_numbers)                 → {1, 2, 3} görünür


# Alıştırma 4: Set metodları
# Anlamı:
#   tags = {"python", "code", "learning"}
#   tags.add("practice")    → eleman ekler
#   tags.remove("code")     → eleman siler
#   print(tags)             → güncel hali gösterir


# Alıştırma 5: İki set arasındaki işlemler
# Anlamı:
#   a = {1, 2, 3, 4}
#   b = {3, 4, 5, 6}
#   a & b   → ikisinde de olanlar (kesişim): {3, 4}
#   a | b   → hepsini birleştirir (birleşim): {1, 2, 3, 4, 5, 6}
#   a - b   → sadece a'da olanlar: {1, 2}
