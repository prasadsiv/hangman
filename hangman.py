import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f"choosen word {chosen_word}.")

display = []
for _ in chosen_word:
    display+= "-"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

  #check gussed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if "_" not in display:
                print("You win")

    print(display)
    
    if "-" not in display:
        end_of_game =True
        print("You Win.")
        
