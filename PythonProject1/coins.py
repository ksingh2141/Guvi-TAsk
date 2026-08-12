for a in range(11):  # Rs 1 coins
    for b in range(6):  # Rs 2 coins
        for c in range(3):  # Rs 5 coins
            for d in range(2):  # Rs 10 coins

                if (a * 1 + b * 2 + c * 5 + d * 10) == 10:
                    print("1Rs:", a, "2Rs:", b, "5Rs:", c, "10Rs:", d)