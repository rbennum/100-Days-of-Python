import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [0, 1, 2]
options_visual = [rock, paper, scissors]
clashes = [
    [None, False, True],
    [True, None, False],
    [False, True, None]
]

while True:
    try:
        user_picks = int(input('What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
        print(options_visual[user_picks])
        computer_picks = random.randint(0, 2)
        print("Computer chose:")
        print(options_visual[computer_picks])
        clash_result = clashes[user_picks][computer_picks]
        if clash_result == None:
            print("You're tied!")
        elif clash_result:
            print("You won!")
        else:
            print("You lose!")
        print("------------")
    except KeyboardInterrupt:
        print("Thank you for playing with me.")
        break
    except:
        print("Input is not defined.")
