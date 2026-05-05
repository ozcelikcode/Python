# Fonksiyonlar Pratiği 2
# Fonksiyonları if/else ve döngülerle birlikte kullanma


# Alıştırma 1: Fonksiyon içinde koşul
# Anlamı:
#   def is_even(number):       → sayı çift mi diye kontrol eder
#       if number % 2 == 0:    → çiftse True, tekse False döner
#           return True
#       return False
#   print(is_even(4))          → True yazar
#   print(is_even(7))          → False yazar

def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(6.2)) # false
print(is_even(9))
print(is_even(10))



# Alıştırma 2: Fonksiyon içinde döngü
# Anlamı:
#   def print_list(items):      → listedeki her elemanı yazdırır
#       for item in items:
#           print(item)
#   print_list(["a", "b", "c"]) → a, b, c ayrı satırlarda yazar

def print_list(items):
    for item in items:
        print((item) + " i")
print_list(["a", "b", "c"])


# Alıştırma 3: Fonksiyon fonksiyon çağırır
# Anlamı:
#   def square(n):             → n'nin karesini döndürür
#       return n * n
#   def sum_of_squares(a, b):  → iki sayının karelerini toplar
#       return square(a) + square(b)
#   print(sum_of_squares(3, 4)) → 9 + 16 = 25 yazar

def square(n):
    return n * n
def sum_of_squares(a, b):
    return square(a) + square(b) # topla
print(sum_of_squares(3, 4)) # 3'ün karesi 9, 4'ün karesi 16 == 25


# Alıştırma 4: Listeyi fonksiyona ver, işlenmiş döndür
# Anlamı:
#   def only_evens(numbers):       → listeden sadece çiftleri döndürür
#       result = []
#       for n in numbers:
#           if n % 2 == 0:
#               result.append(n)
#       return result
#   print(only_evens([1,2,3,4,5,6])) → [2, 4, 6] yazar

def only_evens(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result # sonucu döndür
print(only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Bonus: Fonksiyon bir sözlük döndürür
# Anlamı:
#   def make_person(name, age):   → sözlük oluşturup döndürür
#       return {"name": name, "age": age}
#   person = make_person("Sam", 25)
#   print(person["name"])          → "Sam" yazar
