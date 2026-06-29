
# i = 1

# while (i <= 10):
#     print("The Number is: ",i)
#     i = i + 1

# print("==============="*8)

# i = 10
# while(i <=20):
#     print(i)
#     i = i + 1






# import random
# # print(random.random())  # 0 - 1

# # random_number = random.randint(20,100)
# # print((random_number))


# # Guess Random number game
# import random

# # random_number = random.randint(1,10)

# count = 0
# lives = 5
# while True:
#     if count > lives - 1:
#         print("no attempt left")
#         user_input = input("do you want to play again y/n ").lower()
#         if user_input == "y":
#             random_num = random.randint(1, 10)
#             print("random number is ", random_num)
#             count = 0
#         else:
#             print("Thank you playing")
#             break
#     print(f"Remaining attempt", lives - count)
#     count = count + 1
#     user = int(input("enter a number"))
#     if user == random_num:
#         print("guessed successfully")
#         print("attempt", count)
#         user_input = input("do you want to play again y/n ").lower()
#         if user_input == "y":
#             random_num = random.randint(1, 10)
#             print("random number is ", random_num)
#             count = 0
#         else:
#             print("Thank you playing")
#             break
#     else:
#         print("Try Again")




# rock paper Scissor game

import random 

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice: Rock, Paper or Scissors: ")

    print(f"Player : {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie.")
    elif (
        (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
        or (player == "rock" and computer == "scissors")
    ):
        print("You win")
    else:
        print("You loose")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False



# higher lower case

import random
start_new_game = True
while start_new_game :
    guessed_number = None
    number = random.randint(1, 100)
    guess_counter = 0
    life = 10
    print("You have", life, "lives")
    while guessed_number not in range(1,100):
        guessed_number = int(input(f'Enter a number between (1-100): '))
    if guessed_number < 1 or guessed_number > 100:
        print(f"Number out of range try again")
        continue
    while guessed_number != number and life > 0:

        guess_counter = guess_counter + 1
        life = life - 1
        print(f"Your guess was incorrect with {life} lives left ")

        if guessed_number < number:
            print("Guess Higher")
        else:
            print("Guess Lower")
        guessed_number = int(input(f"Guess a number "))
    if life > 0:
        print(
            f"{guessed_number} was correct, you guessed it in {guess_counter + 1} attempt"
        )
    else:
        print(f"You loose the number was {number}")
    start_new_game = input("Would you like to start a new game (y/n) ").lower()
    if not start_new_game == "y":
        start_new_game = False
