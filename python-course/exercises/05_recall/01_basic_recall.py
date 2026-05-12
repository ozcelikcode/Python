# Temel Tekrar - Serbest Yazım
# Bu dosyada referans kod yok. Görevi oku, kendin yaz.
# Takılırsan yapay zekadan ipucu iste — ama direkt cevap değil.


# Task 1: Değişken ve yazdırma
# "Ali" ismini ve 28 yaşını ayrı değişkenlere ata.
# Sonra şunu yazdır: "Merhaba, benim adım Ali ve 28 yaşındayım."
# f-string kullan.

name = "Ali"
age = 22
print(f"Hello, I am {name} and I am {age} years old")

# Task 2: Basit hesap
# Kullanıcıdan iki sayı al.
# Toplamını, farkını ve çarpımını ayrı satırlarda yazdır.
# Örnek çıktı:
#   Total: 15
#   Difference: 5
#   Product: 50


# Task 3: if/elif/else
# Kullanıcıdan bir not al (0-100 arası).
# 90 ve üstü → "Pekiyi"
# 70 ve üstü → "İyi"
# 50 ve üstü → "Geçer"
# 50'den az  → "Kaldı"

note = int(input("Notunuzu giriniz: "))

if note > 100:
    print("Notunuz 100'den fazla olamaz")
elif note >= 90:
    print("Pek iyi")
elif note >= 70:
    print("İyi")
elif note >= 50:
    print("Normal")
elif note < 0:
    print("Notunuz eksi olamaz")
else:
    print("Maalesef sınavdan kaldın")


# Task 4: for döngüsü
# 1'den 10'a kadar olan sayıları yazdır.
# Ama 5'i atla (continue kullan).
# Örnek çıktı: 1 2 3 4 6 7 8 9 10 (ayrı satırlarda)


# Task 5: while döngüsü
# Kullanıcıdan sayı al. 0 girilince dur.
# Girilen tüm sayıların toplamını en sonda yazdır.
# Örnek:
#   Enter a number: 10
#   Enter a number: 5
#   Enter a number: 0
#   Total: 15


# Task 6: Liste
# 5 farklı meyve ismi içeren bir liste oluştur.
# Listeyi döngüyle gez ve her birini büyük harfle yazdır.
# Örnek çıktı:
#   APPLE
#   BANANA
#   ...


# Task 7: Dictionary
# Bir kişinin adını, yaşını ve şehrini tutan bir sözlük oluştur.
# Anahtarlar İngilizce olsun: name, age, city
# Sözlüğü döngüyle gez, her anahtar-değer çiftini şöyle yazdır:
#   name: Ali
#   age: 28
#   city: Istanbul


# Task 8: Fonksiyon - return
# İki sayı alıp büyük olanı döndüren bir fonksiyon yaz.
# Fonksiyonu birkaç farklı çiftle test et.
# Örnek:
#   bigger(3, 7)  → 7
#   bigger(10, 4) → 10


# Task 9: Fonksiyon + döngü
# Bir liste alıp içindeki tek sayıları döndüren fonksiyon yaz.
# Örnek:
#   only_odds([1, 2, 3, 4, 5, 6])  → [1, 3, 5]


# Task 10: Fonksiyon + dictionary
# İsim ve puan alıp {"name": ..., "score": ..., "passed": ...} döndüren fonksiyon yaz.
# passed: puan 50 ve üstüyse True, değilse False olsun.
# Sonucu yazdır.
# Örnek:
#   make_result("Ayse", 75) → {"name": "Ayse", "score": 75, "passed": True}
