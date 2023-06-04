

fruits = ['apple', 'lemon', 'mango', 'kiwi', 'cherry']
# new_list = []
# for fruit in fruits:
#     new_list.append(fruit[::-1])
#
# print(new_list)

# list comprehension

new_list = [fruit[::-1] for fruit in fruits]

print(new_list)


