import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']


word = random.choice(words)


scrambled = ''.join(random.sample(word, len(word)))

print(" Scramble Game!")
print("Unscramble the word:", scrambled)


guess = ""

while guess != word:
    guess = input("Enter your guess: ")

    if guess == word:
        print("Correct! You guessed the word.")
    else:
        print("Wrong guess. Try again!")

print("The word was:", word)