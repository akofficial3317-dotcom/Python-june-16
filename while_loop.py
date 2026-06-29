
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




