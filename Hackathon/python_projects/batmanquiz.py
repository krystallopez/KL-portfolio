print(''' 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MM.:  .:'   `:::  .:`MMMMMMMMMMM|`MMM'|MMMMMMMMMMM':  .:'   `:::  .:'.MM
MMMM.     :          `MMMMMMMMMM  :*'  MMMMMMMMMM'        :        .MMMM
MMMMM.    ::    .     `MMMMMMMM'  ::   `MMMMMMMM'   .     ::   .  .MMMMM
MMMMMM. :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: ::.MMMMMM
MMMMMMM    ;::         ;::         ;::         ;::         ;::   MMMMMMM
MMMMMMM .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `::MMMMMMM
MMMMMM'     :           :           :           :           :    `MMMMMM
MMMMM'______::____      ::    .     ::    .     ::     ___._::____`MMMMM
MMMMMMMMMMMMMMMMMMM`---._ :: ::'  :   :: ::'  _.--::MMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMM::.         ::  .--MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-.     ;::-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM. .:' .M:F_P:MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.   .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\ /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMVMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=comics/batman
''')

# This is the welcome statement
print("Welcome to the Batman quiz, let's test your knowledge of the Dark Knight")

# This asks the user if they want to play the game
playing = input("Do you want to play ? Type Y for 'yes' and N for 'no'\n")

correct_question = 0  # Will count how many questions the user got correct

if playing == "N".lower():
    quit()  # This will quit the game if the user answers no
elif playing == "Y".lower():
    print("Okay, let's play!")

print("Alright let's start with our first question!\n")
response_1 = input(
    "Question 1: What super villain once broke Batman's back, leaving him crippled and wheelchair-bound?\n")

if (response_1.lower() == "Bane".lower()):
    correct_question += 1
    print("\nCorrect! You got it!\n")
else:
    print("Sorry, the correct answer is Bane. Have you ever even read a comic book?!\n")


print("Second question!\n")
response_2 = input("Question 2: Who is credited with creating Batman?\n")

if (response_2.lower() == "Bob Kane".lower()):
    correct_question += 1
    print("\nCorrect! Good Job!\n")
else:
    print("WRONG!, the correct answer is Bob Kane. Better luck on the next question\n")


print("You are on fire, let's keep it going!\n")
response_3 = input("Question 3: What was Batman's other identity?\n")

if (response_3.lower() == "Bruce Wayne".lower()):
    correct_question += 1
    print("\nCorrect! You got that one right!\n")
else:
    print("Darn, the correct answer is Bruce Wayne. You are a really bad at this.\n")


print("Onto the next question\n")
response_4 = input("Question 4: What is the Riddler's real name?\n")

if (response_4.lower() == "Edward Nigma".lower()):
    correct_question += 1
    print("\nCorrect! Good Job! The Riddler would be proud!\n")
else:
    print("Sorry, the correct answer is Edward Nigma.\n")


print("Let's keep the momentum going..\n")
response_5 = input("Question 5: What was the name of Bruce Wayne's butler?\n")

if (response_5.lower() == "Alfred".lower()):
    correct_question += 1
    print("\nCorrect! Good Job!\n")
else:
    print("Sorry, the correct answer is Alfred. C'mon, you gotta know some of the answers to some of these questions!\n")


print("We are almost at the finish line1 \n")
response_6 = input("Question 6: On Batman: The Animated Series, who was the voice of the Joker?... Here's a hint, the actor who voices the Joker, was also a famous Jedi in the original Star Wars Trilogy. Can you guess who it is?!\n")

if (response_6.lower() == "Mark Hamill".lower()):
    correct_question += 1
    print("\nCorrect! You are really good at this game!\n")
else:
    print("Sorry, the correct answer is Mark Hamill. Clearly, the force is not strong with you.\n")


print("Ooo this next one, is a tough one!\n")
response_7 = input("Question 7: What was Harley Quinn's real name?\n")

if (response_7.lower() == "Harleen Quinzel".lower()):
    correct_question += 1
    print("\nCorrect! You must be Harley's biggest fan!... I don't think the joker would like that!\n")
else:
    print("Sorry, the correct answer is Harleen Quinzel. That's okay, this one was a tough one.")


print("This one is an easy one! You'll get it for sure!\n")
response_8 = input("Question 8: What is the name of Batman's sidekick?\n")

if (response_8.lower() == "Robin".lower()):
    correct_question += 1
    print("\nCorrect! Good Job! I knew you would know this one!\n")
else:
    print("Sorry, the correct answer is Robin. Maybe this one wasn't so easy after all..")


print("Second question!\n")
response_9 = input(
    "Question 9: Who is voiced Batman in Batman: The Animated Series?\n")

if (response_9.lower() == "Kevin Conroy".lower()):
    correct_question += 1
    print("\nCorrect! Good Job! He was the best Batman of all time.\n")
else:
    print("Sorry, the correct answer is Kevin Conroy.")

print("Okay this is the last question.\n")
response_10 = input(
    "Question 10: When did Batman: The Animated Series debut?\n")

if response_10.lower() == "1992".lower():
    correct_question += 1
    print("\nCorrect! Good Job! I was only 2 when this came out!\n")
else:
    print("Sorry, the correct answer is 1992.\n")

print("That's the end of the quiz!\n")
print(f"You got {correct_question} out of 10 questions right, nice!\n")
print("Thank you for playing! This quiz was created in loving memory of Kevin Conroy, the Dark Knight himself. Thank you for being everyone's favorite Batman. You will be missed greatly.\n")

print('''I am Vengeance, I am the Night, I am Batman!                                       

                                        |
                                        |
                                 _______|L
                            .-"""       | \-.
                         .-'            |  \ `-.
                       .'               |   \   `.
                     .'    |            |    \    \
                    /      |L           |     L    `.
                   /       |J           |     J      \
                  /        | \        .-|      \      L
                 J         |  \   .-'" _|       \     \
                 F         |   \.'   .'          \     \
                J          |  .'  .'              \     L
                F          |.' .'                  \    |          .-.
               |           | .'                     \   |        .'   \
               |           | .                       \  |      .'      `.
               |           |.                         \ |    .'
               |           |                           \    /
                L          J                  /|        \ .'
                J           L                / |         /     .-"    "
                 \          \               /  |       .'    .       .
                  \          \              /  |      /   .'
                   \          |            /   |     /  .'
                    `.         \-.__      '----'   .' .'
                      \        |\   `--.          /  '
                       `-.      \\     /        .' .'
                    ____  `-.    \\`--'        / .'
               __.-'    |    `--._\           / .
           _.-'     .-. |          \         / .
        .-'    _   |  | |           \       / .
      .'   .- | \  |  | |            \     J .
     / .') F| |  | J  J  L         .'      F.
    /.' / / | |   \ L  \ \       .' .'    /
  .'   J J  | |    L \  \ \    .' .'     / '
.'     | |  | |    \ L   \ \ .' .'      / '
       | |  | |     \ \   \ \ .'       J .
       F F  J J      L L   \ \         / .
      J J   J J       \ \   \ \       / .
      | |    L L       \ \   `.`.    / .
      | |    | |        \ \    `.`. / .
      F F    J J         \ \     `." :
     J J      L L         \ \      `.:
     | |      J J          \ `.
     | |       L L          `. `.
     | |       J J            `. `.
     | |        \ \             `. `.
     | |         L L              `. `.
     | |         \ \                `. `.
     | |   -      \ \ --      ----    `| `.|       --      |\ |
     | |  | |      \ |  |      |       |`. |.     |  |     | \|
     | |  |--\      \|--|      |          `-.`-   |--|     |  |
     | |  |   \      | \|      |      |  |   `-.`-|  |     |  |
     | |  |    |     |\ |      |      |     |   `-|`-|_    |  |
     | |  |    |     | \|\     |      |     |     |`-| `-. |  |
     J J  |   /      |  | \    |      |     |     |  |`-._`|._|
      L L |--'       |  |\ \   |     |      |     |  |    `|. |-.
      | |                 `.`.                               `-._`-._
      J J                   \ \                                  `-._`-.
       L L                   `.`.                                    `-.
       J J                     `.`.
        L L                      `.`.

                         R.I.P Kevin Conroy 

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=comics/batman
 ''')
