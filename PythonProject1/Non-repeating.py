numbers = [10, 20, 30, 20, 10, 40, 30]

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break