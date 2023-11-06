import random
    
colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE']
colors_map = {1:'RED', 2:'ORANGE', 3:'YELLOW', 4:'GREEN', 5:'BLUE', 6:'PURPLE'} #use codes to represent the colors
guess_colors = ['', '', '', ''] #to change the input integers into the color strings
chances = 10 #users only have 10 chances
turn = 0 #keep track of how many times the users guessed
cont = 0 #flag to stop the loop
passcode = random.choices(colors, k=4) #to select 4 colors at random


def print_start(): #game heaading
    print("-----------------------------------------------------------")
    print("                              MASTERMIND GAME")
    print("-----------------------------------------------------------")
    print("Your are required to find out the 4 colors in the passcode.")
    print("You have 10 chances to guess.")
    print("Here is the list of colors you may choose from:")
    print("__________________________________________________________________________")
    print("       RED    ORANGE    YELLOW    GREEN    BLUE    PURPLE")
    print("__________________________________________________________________________")
    print("Please enter codes to represent the colors as below:")
    print(" ")
    print("1:'RED', 2:'ORANGE', 3:'YELLOW', 4:'GREEN', 5:'BLUE', 6:'PURPLE'")
    print("Example: YELLOW RED BLUE PURPLE --> 3 1 5 6")
    print(" ")
    print("NOTE: COLORS CAN BE REPREATED IN THE PASSCODE" )
    print("__________________________________________________________________________")


def show_hint(): #function to tell users the number of correct colors
    print("Turn: " , turn , "/10")
    print("Correct colours in the right position: ", correct)
    print("Correct colours in the wrong position: ", wrng_pos)
    print(" ")
    print("__________________________________________________________________________")


def win(): #function to print out after winning
    print("           CONGRATUALTIONS! YOU GOT IT RIGHT!")
    print("    The answer was: ", passcode)
    print("             You got it right in", turn, " tries!")
    print("__________________________________________________________________________")


def lose(): #function to print out after finishing the chances
    print("            OH NO! YOU HAVE LOST THE GAME")
    print("    The answer was:" , passcode)
    print("                    Better luck next time!")
    print("___________________________________________________________________________")
    

    
print_start()
while cont == 0:
    try:
        guess = list(map(int, input("Enter your choice of colours: ").split()))
    except ValueError: #when users' inputs are not integers
        print("PLEASE ONLY ENTER CODES TO REPRESENT THE COLORS")
        print(" ")
        continue
    
    if len(guess)!= 4: #when user enters lesser or more than 4 codes
        print("PLEASE ENTER 4 CODES WITH SPACE IN BETWEEN")
        print(" ")
        continue
    
    in_range = 0 #a flag to detect if the codes entered are in the list
    for x in guess:
        if x<1 or x>7:
            in_range = 1
            
    if in_range == 1: 
        print("PLEASE ONLY ENTER CODES FROM THE LIST")
        print(" ")
        continue


    for i in range(4):
        guess_colors[i] = colors_map[guess[i]]  #change code into color string

    print(guess_colors)
    
    correct = 0
    wrng_pos = 0 
    
    for i in range(4):
        if guess_colors[i] == passcode[i]: #correct color in correct position
            correct += 1
        else:
            for j in guess_colors:
                if j == passcode[i] and j != passcode[guess_colors.index(j)]: #correct color in wrong position
                    wrng_pos += 1

    turn += 1 #increase turn everytime they guess
    show_hint()


    if correct == 4: #when users get all 4 correct they win
        cont = 1
        win()

    if turn == chances: #when users used up all the tries
        cont = 1
        lose()
       
        
        

    
