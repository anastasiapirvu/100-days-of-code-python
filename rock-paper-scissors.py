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


# Save input for human

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n."))

# Choose randomly between r, p, s for computer
computer = random.randint(0, 2)


rock == 0
paper == 1
scissors == 2


# Decide who won + display results

if human == 0 and computer == 0:
  print(f"You chose: \n {rock}\n Computer chose: \n {rock} \n It's a draw!")
elif human == 0 and computer == 1:
  print(f"You chose: \n {rock} \n Computer chose: \n {paper} \n You lose!")
elif human == 0 and computer == 2:
  print(f"You chose: \n {rock} \n Computer chose: \n {scissors} \n You win!")
  
elif human == 1 and computer == 0:
  print(f"You chose: \n {paper} \n Computer chose: \n {rock} \n You win!")
elif human == 1 and computer == 1:
  print(f"You chose: \n {paper} \n Computer chose: \n {paper} \n It's a draw!")  
elif human == 1 and computer == 2:
  print(f"You chose: \n {paper} \n Computer chose: \n {scissors} \n You lose!")
  
elif human == 2 and computer == 0:
  print(f"You chose: \n {scissors} \n Computer chose: \n {rock} \n You lose!")   
elif human == 2 and computer == 1:
  print(f"You chose: \n {scissors} \n Computer chose: \n {paper} \n You win!")
elif human == 2 and computer == 2: 
  print(f"You chose: \n {scissors} \n Computer chose: \n {scissors} \n It's a draw!")     

else: 
  print("You typed an invalid number, you lose!")
