# Dictionary Pratiği


# Alıştırma 1: Dictionary oluşturma ve erişim
# Anlamı:
#   person = {"name": "Alice", "age": 25, "city": "Istanbul"}
#   person["name"]     → "Alice" döner
#   person["age"]      → 25 döner

person = {
    "name": "Sebastian",
    "age": 25,
    "city": "Norway",
    "hobby": "coding python"
}

print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")


# Alıştırma 2: Değer güncelleme ve ekleme
# Anlamı:
#   person["age"] = 26          → mevcut değeri günceller
#   person["country"] = "TR"    → yeni anahtar ekler
#   print(person)               → güncel hali gösterir

person["age"] = 28
person["city"] = "Istanbul"
print(person)


# Alıştırma 3: Anahtar silme
# Anlamı:
#   del person["city"]   → o anahtarı ve değerini siler
#   print(person)        → güncel hali gösterir

del person["hobby"]
print(person)


# Alıştırma 4: Dictionary metodları
# Anlamı:
#   scores = {"math": 90, "english": 75, "science": 85}
#   scores.keys()    → tüm anahtarları verir
#   scores.values()  → tüm değerleri verir
#   scores.items()   → anahtar-değer çiftlerini verir

scores = {"math": 90, "english": 75, "science": 85}
print(scores.keys())
print(scores.values())
print(scores.items())


# Alıştırma 5: Dictionary üzerinde döngü
# Anlamı:
#   for key, value in scores.items():
#       print(key, value)   → her çifti sırayla yazdırır
for key, value in scores.items():
    print(key, value)


# Bonus: get() ile güvenli erişim
# Anlamı:
#   person.get("name")          → değeri döner
#   person.get("phone")         → anahtar yoksa None döner
#   person.get("phone", "yok")  → anahtar yoksa "yok" döner

print(person.get("name"))
print(person.get("state")) # none
print(person.get("state", "değer yok")) # değer yok


# Ödev

# 1. Bir sözlük oluştur İçinde 3 anahtar olsun: name, grade, city Değerlerini kendin belirle. (örn. isim: "Ahmet", not: 70, şehir: "Ankara")
# 2. Notu 10 artır grade anahtarının değerini al, üzerine 10 ekle, geri yaz. (Alıştırma 2'de age'i 28 yaptığın gibi)
# 3. Şehri sil city anahtarını sözlükten tamamen kaldır. (Alıştırma 3'te hobby'yi sildiğin gibi)
# 4. Kalan bilgileri yazdır Sözlüğün son halini ekrana yazdır.

dictionary = {
    "name": "Sam",
    "grade": 82,
    "city": "New York"
}

dictionary["grade"] = 92
del dictionary["city"]

print(dictionary)