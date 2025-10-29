# beyin yanma garantili konu
# input kavramı


# number = int(input("Bir sayı giriniz: "))

# if number < 0:
#     print("Negatif sayının faktöriyeli tanımsızdır.")
# else:
#     factorial = 1
#     i = 2
#     while i <= number:
#         factorial *= i
#         i += 1
#     print(f"{number}! = {factorial}")



# Asal sayı kontrolü

# number = int(input("Asal sayı kontrolü: "))

# prime = True

# for i in range(2, number):
#     if number %i == 0:
#         prime = False
#         break
# if prime == True:
#     print(f"{number} sayısı asaldır.")
# else:
#     print(f"{number} sayısı asal değildir.")



# Bölen bulma

# number = int(input("Bölen bir sayı giriniz: "))

# numberOfDivisors = 0

# for i in range(1, number + 1):
#     if number %i == 0:
#         numberOfDivisors += 1
# print(f"{number} sayısının {numberOfDivisors} adet böleni vardır.")



# Girilen sayıların en büyüğü ve en küçüğünü bulma

# listNumber = []

# for i in range(3):
#     number = int(input("Büyüklük oranı için sayı giriniz: "))
#     listNumber.append(number)

# print(f"En büyük sayı: {max(listNumber)}")
# print(f"En küçük sayı: {min(listNumber)}")



text = input("Metin sayımı için yazınız: ")

dictionary = dict()

for letter in text:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1
for letter, piece in dictionary.items():
    print(letter, piece)