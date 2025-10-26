# if else komutları

a = "10"
b = 10

if a == b: # else yerine (!= -> eşit değil) ifadesi de kullanılabilir
    print("Değer eşittir")
else:
    print("Değer dşit değildir")



color = "Green"

colorSection = "Red"
colorSection2 = "Green"
colorSection3 = "Yellow"

if color == colorSection:
    print("1. renk seçimi aynıdır")
elif color == colorSection2:
    print("2. renk seçimi aynıdır")
elif color == colorSection3:
    print("3. renk seçimi aynıdır")
else:
    print("renk seçimi aynı değildir")



# or (veya), and (ve)
x = 12
y = 16
z = 18
w = 18

if (x < y) or (x > z):
    print("Koşul Doğrudur +")
else:
    print("Koşul Doğru Değildir -")

if (z == w) and (x > y):
    print("Koşul Eşittir +")
else:
    print("Koşul Eşit Değildir -")

if not x == w: # !!! x ile w eşit değildir ve bu doğru mudur?
    print("Koşul Doğru (yanlış olduğu için doğru) +")
else:
    print("Koşul Yanlış (doğru olduğu için yanlış) -")


number_list = [1,2,3,4,5,6,7,8]

number = 8

if number in number_list: # number değeri number_list'de mevcut mu?
    print("Listede bulunuyor +")
else:
    print("Listede bulunmuyor -")


language = "python"
l = "p" # P ≠ p

if l in language:
    print("Harf kelime içinde bulunuyor +")
else:
    print("Harf kelime içinde bulunmuyor -")


# is konusu biraz karışıktır, yazmadım