# For / While pratigi

# Alistirma 1:
# MANTIK: "for i in liste" der ki:
#   "listedeki her elemani sirayla al, i'ye ver, altindaki kodu calistir"
#   i sadece bir degisken ismi, n, x, eleman gibi de yazabilirsin.

number_list = [3, 6, 9, 12, 14]

for i in number_list:
    print(i)



# Alistirma 2:
# MANTIK: range(1, 11) -> 1'den basla, 11'e KADAR git (11 dahil degil)
#   Yani 10'u dahil etmek icin bitis degerine +1 ekle.

for i in range(1, 11):
    print(i)



# Alistirma 3:
# MANTIK: Dongu icinde if koyduk.
#   Her eleman icin: "bu sayi 2'ye tam bolunuyor mu?" diye sor.
#   % (modulo) bolumden kalani verir. Kalan 0 ise -> cift.

mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in mixed_numbers:
    if number % 2 == 0:
        print(number)



# Alistirma 4:
# MANTIK: while, kosul dogruyken calisir.
#   x <= 50 oldugu surece dongu devam eder.
#   Her adimda x'e sayı ekle, yoksa sonsuza gider!

x = 1
while x <= 50:
    print(x)
    x += 10



# Alistirma 5:
# MANTIK: input() her zaman string verir, int(...) ile sayiya ceviriyoruz.
#   1'den baslayip dahil etmek icin range(1, sayi+1) kullanalim.

limit = int(input("Enter a number: "))

for i in range(1, limit + 1):
    print(i)



# Bonus:
# MANTIK: break, donguyu aninda durdurur.
#   "muzzo"yu bulunca yazdir ve dur, geriye kalan elemanlara bakma.

fruit_list = ["armutes", "cileks", "elmaa", "muzzo", "kivivi"]

for fruit in fruit_list:
    if fruit == "muzzo":
        print("Found " + fruit)
        break