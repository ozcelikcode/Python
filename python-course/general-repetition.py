from fileinput import filelineno


prime_list = list()

prime_list.append(2)

number = 3

while True:
    prime = True
    for i in range(2, number):
        if number %i == 0:
            prime = False
            break
    if prime:
        prime_list.append(number)
        if len(prime_list) == 10:
            break
    number += 1

print(prime_list)



# fibonacci sayı dizisi

fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

index = 2
while True:
    fibonacci_list.append(fibonacci_list[index - 2] + fibonacci_list[index - 1])
    index += 1
    if len(fibonacci_list) == 100:
        break

print(fibonacci_list)

# diğer bütün örneklere buradan ulaşabilirsin: https://www.youtube.com/watch?v=K9YaA8VYYyo&list=PL3kMAPso9YQ1Ls-5uTTIWWMkJoF_vyj5J