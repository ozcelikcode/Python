# Fonksiyonlar Pratiği


# Alıştırma 1: Basit fonksiyon
# Anlamı:
#   def greet(name):       → fonksiyon tanımla, name parametresi alır
#       print("Hello", name) → çağrılınca bu satırı çalıştırır
#   greet("Sam")           → fonksiyonu çağır

def greet(name):
    print("Hello", name)
greet("Sam")


# Alıştırma 2: return kullanan fonksiyon
# Anlamı:
#   def square(number):    → sayının karesini hesaplar
#       return number * number  → sonucu geri döndürür (print değil!)
#   result = square(5)     → dönen değeri result'a atar
#   print(result)          → 25 yazar

def square(num):
    return num * num
result = square(15)
print(result) # 225


# Alıştırma 3: Birden fazla parametre
# Anlamı:
#   def add(a, b):         → iki parametre alır
#       return a + b       → toplamı döndürür
#   print(add(3, 7))       → 10 yazar

def add(a, b):
    return a / b
print(add(10, 2)) # a, b => 10 / 2 = 5.0


# Alıştırma 4: Liste alan fonksiyon
# Anlamı:
#   def find_max(numbers):      → liste alır
#       return max(numbers)     → en büyük değeri döndürür
#   find_max([4, 8, 15, 23])    → 23 döner

def find_max(numbers):
    return max(numbers) # max olanı bul
print(find_max([30, 2, 5.2, 80, 10, 500, 500.1]))


# Bonus: Varsayılan parametre değeri
# Anlamı:
#   def greet(name, language="EN"):  → language verilmezse "EN" kullanılır
#   greet("Sam")                     → "EN" ile çalışır
#   greet("Sam", "TR")               → "TR" ile çalışır

def greet(name, language="EN"):
    greet("Sam")
    greet("Sam", "TR")