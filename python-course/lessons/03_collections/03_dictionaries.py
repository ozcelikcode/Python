# Dictionaries

example = {
    "Name" : "Suleyman",
    "Age" : 21,
    "Hobies" :  [
        "Cinema",
        "Software Coding",
        "Reading Quran"
    ]
}

print(example["Name"]) # name'i getir

example.update({"Name" : "Gülsena", "Age" : 24}) # name'i değiştir
print(example["Name"])

example["id"] = 1 # id'i dıştan ekle
print(example)

del example["id"] # id'i sil
print(example)


print(example.keys())


# Değeri tam ve alt alta göstermek
for k,v in example.items():
    print(k,v)


# Değer mevcut mu?
print(example.get("id", "Not Found")) # bulunursa, bulunmazsa