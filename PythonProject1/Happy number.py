numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = []

for num in numbers:
    n = num
    visited = []

    while n != 1 and n not in visited:
        visited.append(n)
        sum = 0

        for digit in str(n):
            sum += int(digit) ** 2

        n = sum

    if n == 1:
        happy_numbers.append(num)

print("Happy Numbers:", happy_numbers)
print("Total Happy Numbers:", len(happy_numbers))