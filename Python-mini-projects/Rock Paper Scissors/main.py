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
game2 =['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
choice = int(input("What is your choice? 0 for rock, 1 for paper, 2 for scissors"))
if choice == 0:
    print (f"choice is rock\n{rock}")
elif choice == 1:
    print (f"choice is paper\n{paper}")
elif choice == 2:
    print (f"choice is scissors\n{scissors}")
else:
    print("Invalid choice, Start again!!")
game = [0, 1, 2]
choice_computer = random.choice(game)
computer = ["rock", "paper", "scissors"]
if computer[choice_computer] == "rock" and choice == 0:
    print(f"{rock}\n Its a Draw")
elif computer[choice_computer] == "paper" and choice == 1:
    print(f"{paper}\n Its a Draw")
elif computer[choice_computer] == "scissors" and choice == 2:
    print(f"{scissors}\n Its a Draw")
elif computer[choice_computer] == "rock" and choice == 1:
    print(f"{rock}\n You Win")
elif computer[choice_computer] == "paper" and choice == 2:
    print(f"{paper}\n You Win")
elif computer[choice_computer] == "scissors" and choice == 0:
    print(f"{scissors}\n You Win")
else:
    print(f"{game2[choice_computer]}\n You Lose")