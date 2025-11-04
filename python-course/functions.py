# Functions

def hello(name):
    print("Hello", name)

hello("Admin")


def average_calculation(nlist):
    total = sum(nlist)
    piece = len(nlist)
    average = total / piece
    print(f"Sayıların ortalaması: {average}")

average_calculation([1, 2, 3, 4, 5, 6, 7, 8])



def upper_text(text):
    return text.upper()

upper = upper_text("bu metindeki harflerin tamamı büyük gösterilecektir.")
print(upper)

# daha fazla detay ve örnek için : https://www.youtube.com/watch?v=_HRn8zB47cs&list=PL3kMAPso9YQ1Ls-5uTTIWWMkJoF_vyj5J&index=10