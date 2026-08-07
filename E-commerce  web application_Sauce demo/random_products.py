import random


class RandomProducts:
    """
    Random helper methods.
    """

    @staticmethod
    def choose(products, count=4):

        if count > len(products):
            raise ValueError(
                "Requested count exceeds list size."
            )

        return random.sample(products, count)

    @staticmethod
    def choose_one(products):

        return random.choice(products)