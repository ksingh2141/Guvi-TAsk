numbers = [10, 20, 30, 9]
target = 59

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):

            if numbers[i] + numbers[j] + numbers[k] == target:
                print("Triplet is:", numbers[i], numbers[j], numbers[k])