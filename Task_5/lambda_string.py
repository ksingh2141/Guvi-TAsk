def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

print(is_number("123"))
print(is_number("45.6"))
print(is_number("hello"))