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

jo_ken_po = [rock, paper, scissors]
try:
    player_choice = int(input('Choice one (input the matching number): rock[0], paper[1], scissor[2]\n'))
    if player_choice >= 0 and player_choice <= 2:
        print(f'You chose{jo_ken_po[player_choice]}')

    computer_choice = random.randint(0,2)
    print(f'The computer chose{jo_ken_po[computer_choice]}')
except ValueError:
    print("You need to choose an integer number!")
else:
    if player_choice >= 3 or player_choice < 0:
            print('ERROR! You chose an invalid number! You LOSE!')
    else:
        if computer_choice == player_choice:
            print("It's a draw!")
        elif player_choice == 2 and computer_choice == 0:
            print('You LOSE!')
        elif player_choice == 0 and computer_choice == 2:
            print('You WIN!!')
        elif computer_choice > player_choice:
            print('You LOSE!')
        elif player_choice > computer_choice:
            print('You WIN!!')
