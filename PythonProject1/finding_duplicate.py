list1 = [10, 501, 22, 37, 100, 999, 87, 351]
list2 = [19, 51, 22, 37, 180, 909, 87, 351]
list3 = [10, 51, 22, 38, 100, 999, 87, 351]

duplicates = []

for num in list1:
    if num in list2 and num in list3:
        duplicates.append(num)

print("Duplicate numbers in all three lists:", duplicates)