# Demet ve Küme Kavramları (Tuples and Sets)

colors = ("Black", "Blue", "Gray", "White", "Pink")

for color in colors:
    print(color)



# Küme nedir? nasıl kullanılır?

clusterColors = {"Orange", "Green", "Purple"}
print(type(clusterColors))

for cc in clusterColors:
    print(clusterColors)

clusterColors.discard("Gray") # var mı yok mu ara, hata vermez
print(clusterColors)



# ortak bulma
clusterColors2 = {"Black", "Purple", "Blue"}
clusterColors3 = {"Gray", "Purple", "Blue", "Green"}
print(clusterColors2.intersection(clusterColors3))

# birleşim
print(clusterColors2.union(clusterColors3))

# karşı değerdekinde eksik bulma
print(clusterColors2.difference(clusterColors3))

print("White" in clusterColors2) # var mı?



text = set("Python")
print(text)

number = set([1,2,3,4,5])
print(number)