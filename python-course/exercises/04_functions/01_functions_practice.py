# Fonksiyonlar Pratiği


# Alıştırma 1: Basit fonksiyon
# Anlamı:
#   def greet(name):       → fonksiyon tanımla, name parametresi alır
#       print("Hello", name) → çağrılınca bu satırı çalıştırır
#   greet("Sam")           → fonksiyonu çağır


# Alıştırma 2: return kullanan fonksiyon
# Anlamı:
#   def square(number):    → sayının karesini hesaplar
#       return number * number  → sonucu geri döndürür (print değil!)
#   result = square(5)     → dönen değeri result'a atar
#   print(result)          → 25 yazar


# Alıştırma 3: Birden fazla parametre
# Anlamı:
#   def add(a, b):         → iki parametre alır
#       return a + b       → toplamı döndürür
#   print(add(3, 7))       → 10 yazar


# Alıştırma 4: Liste alan fonksiyon
# Anlamı:
#   def find_max(numbers):      → liste alır
#       return max(numbers)     → en büyük değeri döndürür
#   find_max([4, 8, 15, 23])    → 23 döner


# Bonus: Varsayılan parametre değeri
# Anlamı:
#   def greet(name, language="EN"):  → language verilmezse "EN" kullanılır
#   greet("Sam")                     → "EN" ile çalışır
#   greet("Sam", "TR")               → "TR" ile çalışır
