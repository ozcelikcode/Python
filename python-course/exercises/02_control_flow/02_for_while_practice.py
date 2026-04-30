# For / While pratigi
#
# Bu dosyada amac, for ve while dongu mantigini kendi basina denemek.
# Once yorumlari oku, anla, sonra kendi basina tekrar yazmaya calis.


# ---------------------------------------------------------------
# Alistirma 1:
# [1, 2, 3, 4, 5] listesindeki her elemani ekrana yazdir.
#
# MANTIK: "for i in liste" der ki:
#   "listedeki her elemani sirayla al, i'ye ver, altindaki kodu calistir"
#   i sadece bir degisken ismi, n, x, eleman gibi de yazabilirsin.
#
# KOPYA:
#   number_list = [1, 2, 3, 4, 5]
#   for i in number_list:
#       print(i)
# ---------------------------------------------------------------

number_list = [1, 2, 3, 4, 5]

# Kodunu buraya yaz:


# ---------------------------------------------------------------
# Alistirma 2:
# range() kullanarak 1'den 10'a kadar olan sayilari yazdir.
# (10 dahil olmali)
#
# MANTIK: range(1, 11) -> 1'den basla, 11'e KADAR git (11 dahil degil)
#   Yani 10'u dahil etmek icin bitis degerine +1 ekle.
#
# KOPYA:
#   for i in range(1, 11):
#       print(i)
# ---------------------------------------------------------------

# Kodunu buraya yaz:


# ---------------------------------------------------------------
# Alistirma 3:
# Asagidaki listede sadece cift sayilari yazdir.
#
# MANTIK: Dongu icinde if koyduk.
#   Her eleman icin: "bu sayi 2'ye tam bolunuyor mu?" diye sor.
#   % (modulo) bolumden kalani verir. Kalan 0 ise -> cift.
#
# KOPYA:
#   for sayi in mixed_numbers:
#       if sayi % 2 == 0:
#           print(sayi)
# ---------------------------------------------------------------

mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Kodunu buraya yaz:


# ---------------------------------------------------------------
# Alistirma 4:
# 1'den baslayip 5'er 5'er artan, 50'yi gecmeden sayilari yazdir.
# Bunu while dongusuyle yap.
#
# MANTIK: while, kosul dogruyken calisir.
#   x <= 50 oldugu surece dongu devam eder.
#   Her adimda x'e 5 ekle, yoksa sonsuza gider!
#
# KOPYA:
#   x = 1
#   while x <= 50:
#       print(x)
#       x += 5
# ---------------------------------------------------------------

# Kodunu buraya yaz:


# ---------------------------------------------------------------
# Alistirma 5:
# Kullanicidan bir sayi al.
# O sayiya kadar olan sayilari for ile yazdir.
#
# MANTIK: input() her zaman string verir, int(...) ile sayiya ceviriyoruz.
#   1'den baslayip dahil etmek icin range(1, sayi+1) kullanalim.
#
# KOPYA:
#   limit = int(input("Bir sayi gir: "))
#   for i in range(1, limit + 1):
#       print(i)
# ---------------------------------------------------------------

# Kodunu buraya yaz:


# ---------------------------------------------------------------
# Bonus:
# Asagidaki listede "elma" kelimesini bul.
# Buldugunda "Elma bulundu!" yazdir ve donguyu durdur.
# Bulamazsan hicbir sey yazma.
#
# MANTIK: break, donguyu aninda durdurur.
#   "elma"yi bulunca yazdir ve dur, geriye kalan elemanlara bakma.
#
# KOPYA:
#   for meyve in fruit_list:
#       if meyve == "elma":
#           print("Elma bulundu!")
#           break
# ---------------------------------------------------------------

fruit_list = ["armut", "cilek", "elma", "muz", "kivivi"]

# Kodunu buraya yaz:
