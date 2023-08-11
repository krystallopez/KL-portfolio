# This is the final code for the Hangman game from Python 100 Days, I built out this code following the video provided in the 100 Days of Code: The Complete Python Pro Bootcamp for 2023

import random
from word_list_hangman import word_list
from art_hangman import stages
from art_hangman import logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_end = False
user_lives = 6

print(logo)

# print(f"Psst the word is {chosen_word}")
display_blanks = []
for letter in chosen_word:
    display_blanks += "_"

while not game_end:
    guess = input("Guess a letter: ").lower()
    if guess in display_blanks:
        print(f"Oh dear, looks like you have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display_blanks[position] = letter
    if guess not in chosen_word:
        user_lives -= 1
        print(
            f"You have guessed {guess}, that letter is not in the word. You have {user_lives} lives left.")
        if user_lives == 0:
            game_end = True
            print("You lose.")

    print(f"{' '.join(display_blanks)}")

    if "_" not in display_blanks:
        game_end = True
        print("You win.")

    print(stages[user_lives])


# Welcome to Hangman: Here's how it works...

# 1. On line 3, I am importing the random module so that the console is able to randomly choose an item. On lines 2 - 60, the stages list was added to show the stages a user will go through each time they guess a letter wrong. Each time a user guess a letter wrong another limb is added to the hangman. For a better user experience, I created a file that contained the new words_list and imported the file into this one. You can see that this was done on line 4. On lines 5 and 6 I have imported the stages list and the logo variable from the arthangman file as well.

# 2. The chosen_word variable on line 8,uses the random module and choice method to randomly choose a word from the word_list and assigns it to the chosen_word variable.

# 3. The for-in loop on lines 18-20 adds an underscore to the display_blanks list for every letter in chosen_word. The print statement on line 20, prints out the display_blanks list of empty underscore strings. I then printed the display_blanks list to show the list of underscore strings or blanks that need to be filled.

# 4. On line 11, I created the variable game_end and set it to false, because it is not yet the end of the game. On lines 21, I used a while loop around the block of code so that from lines 21-40, the user can continue to guess a letter if the letter that they guesses was not included in the word. The while loop will stop once the user has guessed all of the letters. While game_end or while not game_end, the code block will repeat until all all of the blanks are filled. The guess variable on line 22 stores the user input into a variable. If you take a look at line 23-24, if the user has already guessed a specific letter, a print statement will print to the console letting them know that they have already guessed that letter.

# 5. The for-in loop on line 26, will match the letter to the position that it holds in the word and will then add it to the display_blanks list, once display_blanks is printed to the console the letters will appear the position that they are located in the chosen_word.

# 6. I created a variable called user_lives to keep track of the number of user_lives the user has left. I have set the value of user_lives to equal 6. The print statement on line 35 will join all of the elements of the list and turn it into a string. If the guess is not a letter that is in the random word that was chosen from the word_list, the number of user_lives decrease by 1, as shown on line 29. Once the user has guessed the letter incorrectly, a print statement will be printed to the console letting them know the letter is not in the word as well as how many lives they have left.  On line 31, if user_lives goes down to 0 then "you lose", will be printed to the console.

# 7. On line 37, If there are no more blanks then game_end is changed to true and the user has won the game. The display_blanks is printed through steps 4-6 to show each letter in its corresponding position.

# 8. The next step is that I want to print the ASCII aet from the stages list that corresponds to the current number of user_lives that the user has left. In order to do this, all we have to is the stages list and use the user_lives variable as the corresponding number of user_lives, if the number of user_lives is 3, then it will print out the stage that is at the index of 3.
