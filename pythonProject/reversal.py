number_list = [4, 8, 5, 3, 29, 31, 6, 2, 41, 26]

# Using a for loop to reverse the list
reversed_list = []
for i in range(len(number_list) - 1, -1, -1):
    reversed_list.append(number_list[i])

print(reversed_list)