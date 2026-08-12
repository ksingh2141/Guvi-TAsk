# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_list = []
odd_list = []

# Loop through the list
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)


result = (even_list, odd_list)

print("Even Numbers:", result[0])
print("Odd Numbers:", result[1])