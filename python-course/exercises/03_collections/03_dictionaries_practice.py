# Dictionary Pratiği


# Alıştırma 1: Dictionary oluşturma ve erişim
# Anlamı:
#   person = {"name": "Alice", "age": 25, "city": "Istanbul"}
#   person["name"]     → "Alice" döner
#   person["age"]      → 25 döner


# Alıştırma 2: Değer güncelleme ve ekleme
# Anlamı:
#   person["age"] = 26          → mevcut değeri günceller
#   person["country"] = "TR"    → yeni anahtar ekler
#   print(person)               → güncel hali gösterir


# Alıştırma 3: Anahtar silme
# Anlamı:
#   del person["city"]   → o anahtarı ve değerini siler
#   print(person)        → güncel hali gösterir


# Alıştırma 4: Dictionary metodları
# Anlamı:
#   scores = {"math": 90, "english": 75, "science": 85}
#   scores.keys()    → tüm anahtarları verir
#   scores.values()  → tüm değerleri verir
#   scores.items()   → anahtar-değer çiftlerini verir


# Alıştırma 5: Dictionary üzerinde döngü
# Anlamı:
#   for key, value in scores.items():
#       print(key, value)   → her çifti sırayla yazdırır


# Bonus: get() ile güvenli erişim
# Anlamı:
#   person.get("name")          → değeri döner
#   person.get("phone")         → anahtar yoksa None döner
#   person.get("phone", "yok")  → anahtar yoksa "yok" döner
