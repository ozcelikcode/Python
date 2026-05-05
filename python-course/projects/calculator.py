# Hesap Makinesi
# Kullanıcıdan iki sayı ve işlem tipi alır, sonucu yazdırır.


# Adım 1: İşlem fonksiyonları
# Anlamı:
#   def add(a, b):       → toplar, sonucu döndürür
#       return a + b
#   def subtract(a, b):  → çıkarır
#       return a - b
#   def multiply(a, b):  → çarpar
#       return a * b
#   def divide(a, b):    → böler, b sıfırsa uyarı verir
#       if b == 0:
#           return "Sıfıra bölme hatası"
#       return a / b


# Adım 2: Kullanıcıdan girdi al
# Anlamı:
#   a = float(input("Birinci sayı: "))    → ondalıklı sayı alır
#   b = float(input("İkinci sayı: "))
#   op = input("İşlem (+, -, *, /): ")   → işlem sembolü alır


# Adım 3: İşlemi seç ve sonucu yazdır
# Anlamı:
#   if op == "+":
#       result = add(a, b)
#   elif op == "-":
#       result = subtract(a, b)
#   elif op == "*":
#       result = multiply(a, b)
#   elif op == "/":
#       result = divide(a, b)
#   else:
#       result = "Geçersiz işlem"
#   print(f"Sonuç: {result}")
