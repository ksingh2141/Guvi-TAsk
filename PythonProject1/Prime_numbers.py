# Given List
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime_list = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

# Count of prime numbers
count = len(prime_list)

print("Prime Numbers:", prime_list)
print("Total Prime Numbers:", count)