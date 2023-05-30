# zadanie 1: stwórz liste zawierajaca 5 owoców, a nastepnie
# za pomocą pętli for i nowej listy odwróć każdy z tych owoców
#     arbuz => zubra
# wynik (w nowej l   iście) wyprintuj na ekranie

fruits = ['apple', 'lemon', 'mango', 'kiwi', 'cherry']
new_list = []
for fruit in fruits:
    new_list.append(fruit[::-1])

print(new_list)