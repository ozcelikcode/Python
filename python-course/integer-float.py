## Integer & Float

# integer       "int()"
# string        "str()"
# type          "type()"

print("""Integer ve float:""")
a = 10
b = 8.9
x = "10"

collect = a + b

print(collect)
print(int(x) == a) # x değeri integer'a çevrildi, b'ye eşit midir?
print(int(42.3)) # integer sadece tam sayı kısmını alır


print("""
Matematiksel İfadeler:""")
## Matematiksel İfadeler

# Toplama               "+"
# Çıkarma               "-"
# Çarpma                "*"
# Bölme                 "/"
# Tamsayı bölme         "//"
# Kuvvet alma           "**"
# Mutlak değer          "abs"
# Yuvarlama             "round"
# İşlem önceliği        "() veya otomatik"

c = 50
d = 12
f = -14
e = 6.59999999

i = 5.5
i *= 3 # hızlı ve profesyonel kullanım

print(c // d)
print(c / d)
print(c * d)
print(abs(f))
print(round(e, 3)) # 3 adet karakter gösterilir, yuvarlamanın yuvarlaması yapılır



print("""
Karşılaştırma operatörleri:""")
## Karşılaştırma operatörleri

# Eşittir "=="
# Küçüktür "<"
# Büyüktür ">"
# Küçük eşittir "<="
# Büyük eşittir ">="
# Eşit değildir "!"

print(4 == 4) # sayılar arasındaki etkileşimler yorumlanır (True/False)