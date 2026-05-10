# Karışık Tekrar Egzersizleri
# Fonksiyon + döngü + koşul + koleksiyon bir arada


# Egzersiz 1: Fonksiyon + if/else
# Görev: Bir sayının pozitif, negatif veya sıfır olduğunu döndüren fonksiyon yaz.
# Anlamı:
#   def check_number(n):
#       if n > 0:
#           return "pozitif"
#       elif n < 0:
#           return "negatif"
#       else:
#           return "sıfır"
#   print(check_number(5))   → "pozitif"
#   print(check_number(-3))  → "negatif"
#   print(check_number(0))   → "sıfır"

def check_number(n):
    if n > 0:
        return "pozitif"
    elif n < 0:
        return "negatif"
    else:
        return "sıfır"
print(check_number(5))
print(check_number(-20))
print(check_number(0))

# Egzersiz 2: Fonksiyon + döngü + liste
# Görev: Bir liste alıp elemanların toplamını döndüren fonksiyon yaz.
#        Bunu sum() kullanmadan, döngüyle yap.
# Anlamı:
#   def total(numbers):
#       result = 0          → başlangıç değeri 0
#       for n in numbers:
#           result += n     → her elemanı üstüne ekle
#       return result
#   print(total([1, 2, 3, 4, 5]))  → 15

def total (numbers):
    result = 0
    for n in numbers:
        result +=n
    return result
print(total([1, 2, 3, 4, 5])) # 15

# Egzersiz 3: Fonksiyon + dictionary
# Görev: İsim ve yaş alıp dictionary döndüren fonksiyon yaz.
#        Sonra döndürülen sözlüğü döngüyle yazdır.
# Anlamı:
#   def make_profile(name, age):
#       return {"name": name, "age": age}
#   profile = make_profile("Sam", 25)
#   for key, value in profile.items():
#       print(f"{key}: {value}")

def make_profile(name, age):
    return {"name": name, "age": age}
profile = make_profile("Sam", 25)
for key, value in profile.items():
    print(f"{key}: {value}")


# Egzersiz 4: while + fonksiyon
# Görev: Kullanıcıdan sayı al. Çift ise "Çift", tek ise "Tek" yazdır.
#        Kullanıcı "q" yazınca dur.
# Anlamı:
#   def is_even(n):
#       return n % 2 == 0
#   while True:
#       user_input = input("Sayı gir (q = çıkış): ")
#       if user_input == "q":
#           break
#       number = int(user_input)
#       if is_even(number):
#           print("Çift")
#       else:
#           print("Tek")

def is_even(n):
    return n % 2 == 0
while True:
    user_input = input("Sayı gir (q = çıkış): ")
    if user_input == "q":
        break
    number = int(user_input)
    if is_even(number):
        print("Çift")
    else:
        print("Tek")


# Egzersiz 5: Fonksiyon + liste filtreleme
# Görev: Bir liste ve bir eşik değeri alıp, eşikten büyük elemanları döndüren fonksiyon yaz.
# Anlamı:
#   def above_threshold(numbers, threshold):
#       result = []
#       for n in numbers:
#           if n > threshold:
#               result.append(n)
#       return result
#   print(above_threshold([3, 8, 1, 15, 6, 20], 7))  → [8, 15, 20]
