# zadanie 1: stwórz liste zawierajaca 5 owoców, a nastepnie
# za pomocą pętli for i nowej listy odwróć każdyz tych owoców
#     arbuz => zubra
# wynik (w nowej liście) wyprintuj na ekranie

fruits = ['lemon', 'apple', 'orange', 'cherry', 'mango']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.append(fruit[::-1])

print(reversed_fruits)
