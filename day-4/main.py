import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# 1 = Rock, 2= Paper, 3 = Scissors
def rps():
    rand = random.randint(1, 3)
    if rand == 1:
        print(rock)
        return "rock"
    elif rand == 2:
        print(paper)
        return "paper"
    elif rand == 3:
        print(scissors)
        return "scissors"

play_again = "y"
while play_again == "y":
    player_choice = input("rock, paper, or scissors? ").lower()
    computer_choice = rps()
    print("The Computer chose " + computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "scissors") and (computer_choice == "paper"):
        print("You Win!")
    elif (player_choice == "rock") and (computer_choice == "scissors"):
        print("You Win!")
    elif (player_choice == "paper") and (computer_choice == "rock"):
        print("You Win!")
    else:
        print("You Lose!")
    play_again = input("Play again? y/n")
