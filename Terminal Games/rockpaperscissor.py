import random
rock = '''
    ROCKS
    _________
___|     ____)
        (______)
        (_______)
        (______)
____,__(____)
      
'''

paper = '''
    PAPERS
    ________
___'    ____)____
          _______)
         _________)
        _________)
______,_______)

'''

scissors = '''
    SCISSORS
     _________
____'      ____)____
              _______)
           ____________)
           (_____)
______,____(___)

'''

while(1):
    game = [rock, paper, scissors]
    user_input = int(
        input("enter the choice \n 0 - rock\n1 - paper \n 2 - scissor \n"))
    print(game[user_input])
    comp = random.randint(0, 2)
    print(game[comp])
    if user_input > 3 and user_input < 1:
        print("Enter Valid Choice")
    elif user_input == 0 and comp == 2:
        print("you Won !")
    elif user_input == 0 and comp == 1:
        print("you lost !")
    elif(user_input < comp):
        print("you Lost !")
    elif(user_input > comp):
        print("you Won !")
    elif(user_input == comp):
        print("It's a Draw")
