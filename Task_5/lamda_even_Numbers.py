numbers = [1, 2, 3, 4, 5, 6, 7, 8]


is_even = lambda x: x % 2 == 0

squares = [x**2 for x in numbers if is_even(x)]

print(squares)