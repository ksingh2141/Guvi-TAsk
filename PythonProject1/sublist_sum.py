numbers = [4, 2, -3, 1, 6]

found = False

for i in range(len(numbers)):
    total = 0
    for j in range(i, len(numbers)):
        total = total + numbers[j]

        if total == 0:
            print("Sub-list with sum 0 found")
            found = True
            break
    if found:
        break

if not found:
    print("No sub-list with sum 0")