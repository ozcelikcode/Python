import os

print(os.getcwd())
# os.chdir("C:\Users\ozcelik\Documents\")
# print(os.getcwd())


for file in os.listdir():
    print("- ", file) # dosyaları satırlara diz

# oluştur ? klasör bir kere oluşturulabilir, 2. denemede hata verir
os.mkdir("bu-klasor-python-tarafindan-olusturuldu")
os.makedirs("Klasor-1/Klasor-2/Klasor-3")

# sil
os.rmdir("Klasor-1/Klasor-2/Klasor-3")
# os.removedirs("Klasor-1/Klasor-2") # hata verir

os.remove("GEREKSIZ_DOSYA.txt")

# değiştir
os.rename("lists.py", "lesson3-lists.py")

os.rename("GEREKSIZ_DOSYA.txt", "\python-course\Klasor-1") # taşınır

# konu hakkında daha fazla bilgi için: https://www.youtube.com/watch?v=FwpD9m9jWRo&list=PPSV
## os.chdir hata veriyor ilginç bir şekilde. Videoda mac ile gösterilmiş.