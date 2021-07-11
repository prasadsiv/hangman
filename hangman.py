import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f"choosen word {chosen_word}.")

display = []
for _ in chosen_word:
    display+= "-"

guess = input("Guess a letter: ").lower()


for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess

print(display)
