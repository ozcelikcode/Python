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

print("Name:", person["name"], ",",
      "Age:", person["age"], ",",
      "City: ", person["city"], ",",
      "Hobby: ", person["hobby"]
      )


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