# Sayı Tahmin Oyunu
# Bilgisayar 1-100 arası rastgele bir sayı seçer.
# Kullanıcı doğru sayıyı bulana kadar tahmin eder.


# Adım 1: random modülünü içe aktar
# Anlamı:
#   import random              → random modülünü kullanıma açar
#   random.randint(1, 100)     → 1 ile 100 arasında rastgele tam sayı üretir

import random
random.randint(1, 100)

# Adım 2: Gizli sayıyı belirle ve sayacı başlat
# Anlamı:
#   secret = random.randint(1, 100)  → oyunun cevabı, kullanıcı görmez
#   attempts = 0                     → kaç tahminde bulduğunu sayar

secret = random.randint(1, 100)
attempts = 0

# Adım 3: Döngü ile tahmin al
# Anlamı:
#   while True:                          → kullanıcı doğruyu bulana kadar devam et
#       guess = int(input("Tahmin: "))   → kullanıcıdan tahmin al
#       attempts += 1                    → her tahminde sayacı artır
#       if guess < secret:
#           print("Daha büyük!")
#       elif guess > secret:
#           print("Daha küçük!")
#       else:
#           print(f"Doğru! {attempts} tahminde buldun.")
#           break                        → doğru tahmin → döngüyü bitir

while True:
    guess = int(input("Tahmin: "))
    attempts += 1
    if guess < secret:
        print("Daha büyük!")
    elif guess > secret:
        print("Daha küçük!")
    else:
        print(f"Doğru! {attempts}. tahminde buldun. Doğru sayı {secret}")
        break