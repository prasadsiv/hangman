import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f"choosen word {chosen_word}.")

display = []
for _ in chosen_word:
    display+= "-"

guess = input("Guess a letter: ").lower()

position = 0 
for letter in chosen_word:
    if letter == guess:
        display[position] = guess
    position +=1
print(display)
