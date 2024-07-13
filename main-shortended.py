    # elif(computer == 1 and choice == -1):    1-(-1) = 2
    #     print("You lose")        
    # elif(computer == 1 and choice == 0):       1-0 = 1
    #     print("You win")

    # elif(computer == -1 and choice == 0):         -1-0 = -1
    #     print("You lose")
    # elif(computer == -1 and choice == 1):           -1-1 = -2
    #     print("You win")
    # elif(computer == 0 and choice == 1):   0-1 = -1
    #     print("You lose")
    # elif(computer == 0 and choice == -1):   0 - (-1) = 1
    #     print("You win")
#Observe the pattern in the code in cases of loses and wins. in case of lose, its
#either 2 or -1 and in case of wins it's 1 or -2

#Hence, we can replace this entire code by 
# if((computer - choice) == 2 or -1):
#     print ("You lose")

# else:
#     print("You won") 


#Therefore, the code will be:
import random
computer = random.choice([-1, 0, 1])

n = str(input('Choose your weapon (r = rock, p = paper, s = scissors): '))

if n not in ("r","p","s"):
    print("error")
while n not in ("r","p","s"):
    n = str(input('Choose your weapon (r = rock, p = paper, s = scissors): '))
    

else:
    weapon = {"r": 1, "p": 0, "s": -1}
    dict = {1 : "Rock", 0 : "Paper", -1 : "Scissors"}
    choice = weapon[n]


    print("The computer chose:",dict[computer])
    print("You chose:",dict[choice])

    if(computer == choice):
        print("Draw")

if((computer - choice) == 2 or -1):
    print ("You lose")

else:
    print("You won") 