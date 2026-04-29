print("Kaçırma işlemi: ", 'Free \'Palestine') # buradaki kaçırma yapmak için ters slash yapılır.

print("3'lü çift tırnak kullanımı: ", """Selam
      
      
      
      Nasılsın?
      
      
      
      Dünya""") # (""" """) 6 adet çift tırnak içerisinde yazılanlar boşluklar ve satırlar dahil edilir.

print("Satır atlama işlemi: ", "Satır \natlama") # \n -> satır atlar

print("Cümle TAB işlemi: ", "Cümle \t\t\tatlama")



## Değişkenler

comment = "Hello"
space = " "
comment2 = "World!"

print("Çoklu değişken kullanma: ", comment + space + comment2 + " Text" + comment[3] + comment[-2])


element = "Naber dünya?"
password = "skivfjrjeyloixmjeatdijn"

print(element[0:5] + element[11]) # yazının 0-5 arası harflerini alır, yazının 11. karakterini alır
print(password[::2]) # cümlenin +2 şeklinde harflerini alır

print(f"ad: {element}, şifreniz: {password[::2]}")