import random

words = ["python", "programming", "hangman", "computer", "science"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6
used = set()

while tries > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Tries left:", tries)
    print("Used letters:", " ".join(sorted(used)))

    letter = input("Enter a letter: ").lower()

    if letter in used:
        continue

    used.add(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        tries -= 1

if "_" not in guessed:
    print("\nYou win! Word was:", word)
else:
    print("\nYou lose! Word was:", word)