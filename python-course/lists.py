# Listeler

colors = ['Black', 'White', 'Blue', 'Yellow']

# özel ayıklama: (:x), (::x), (x::), (x:x:x) # x = rakam
print("list: ", colors)
print(len(colors))


# Metodlar
# sort sorted ve extend biraz daha kapsamlı, kaynaklardan bakman daha iyi

colors.append("Green") # ekleme yapar
print("append: ", colors)

colors.insert(0, "Gray") # 0. index'e ekle
print("insert: ", colors)

colors.remove("Blue") # siler
print("remove: ", colors)

colors.reverse()
print("reverse: ", colors) # listeyi tamamen tersine çevirir



numbers = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10]

print(min(numbers)) # en küçük sayı
print(max(colors)) # en sondaki
print(sum(numbers)) # toplanır
print("Blue" in colors) # bu değer listede var mı? true/false

colorsString = "-|-".join(colors)
print(colorsString)

colorsString2 = colorsString.split("-")
print(colorsString2)