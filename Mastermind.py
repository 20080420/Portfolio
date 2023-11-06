import random

#starting screen
def intro():
  print("++++++++++++++++++++++++++++++++++++++++")
  print("+        Master Mind with Fruits       +")
  print("+         made by Rachel Foo           +")
  print("++++++++++++++++++++++++++++++++++++++++")
  print("+               Tutorial               +")
  print("+ 1)The game will generate 4 fruits    +")
  print("+   From the list of apple, banana,    +")
  print("+   orange, and lemon.                 +")
  print("+                                      +")
  print("+ 2)The user will have to guess which  +")
  print("+   fruits are in which slot           +")
  print("+                                      +")
  print("+ 3)After each guess, the game will    +")
  print("+   inform the player how many fruits  +")
  print("+   they got right in the correct      +")
  print("+   position, and how many fruits were +")
  print("+   correct but in the wrong position. +")
  print("+                                      +")
  print("+ 4)Be aware that the game can select a+")
  print("+   fruit more than once.              +")
  print("+                                      +")
  print("+ 5)The aim of this game is to find the+")
  print("+   correct sequence with the least    +")
  print("+   guesses. That's all, please enjoy! +")
  print("++++++++++++++++++++++++++++++++++++++++")
  print("")

#hint text displayed after every guess to provide feedback to user
def hint():
  print("  apple | banana | orange | lemon  ")
  print("Guess number: ", gcount)
  print("Correct fruits in the right position: ", correct)
  print("Correct fruits in the wrong position: ", wrongpos)
  print(" ")

#text printed out when user has guessed all 4 fruits correctly
def win():
  print("           Congratulations! You have won the game!")
  print("    The answer was: ", ansfruit)
  print("                  You won in",gcount, " guesses!")
  print("")


intro()
#starting data
availfruits = ["apple", "banana", "orange", "lemon"]
ansfruit = random.choices(availfruits, k=4)
guessfruit = ["", "", "", ""]
gcount = 0
game = True
print(ansfruit)
while game == True:
    #asks for inputs and splits the inputs up
         guess = list(map(str, input("Enter your guess of fruits: ").split()))
    #checks if there are too many or not enough inputs
         if len(guess) != 4:
          print("Please guess 4 fruits with space in between")
          print("  apple | banana | orange | lemon  ")
          print("")
          continue
        #checks whether the inputs are from the availfruits list
         inrange = 0
         for x in guess:
           if x not in availfruits:
             inrange = 1
#display error message if input is not one of the four fruits
         if inrange == 1:
           print("Please only guess fruits in the list.")
           print("  apple | banana | orange | lemon  ")
           print(" ")
           continue
        #changes inputs to string for examination
         for y in range(4):
           guessfruit[y] = str(guess[y])

         print(guessfruit)

         correct = 0
         wrongpos = 0
    #checks whether fruit is correct and in correct position
         for y in range(4):
           if guessfruit[y] == ansfruit[y]:
             correct = correct + 1
           else:
               #checks whether fruit is correct but in wrong position
             for z in guessfruit:
               if z == ansfruit[y] and z != ansfruit[guessfruit.index(z)]:
                 wrongpos = wrongpos + 1
                    #increases guess count to show guess count to user
         gcount = gcount + 1
         hint()
    #checks whether the user win by having all four correct fruits in correct position
         if correct == 4:
           game = False
           win()
           endscreen = "d"
           #puts game into false mode so it loop closes and prompts user whether they want to play again
           while game == False:
               endscreen = input("   Do you want to play again? Type Yes(Y/y) or No(N/n): ").lower()
               print("")
               #if user types N or n msg will be displayed and program will end
               if endscreen == "n":
                   print("Thank you for playing this game! Feel free to play again next time!")
                   print("")
                   exit()
                   #if user types Y or y msg will be displayed and game will start again, resetting guess count and generate new fruit answer
               elif endscreen == "y":
                   intro()
                   gcount = 0
                   ansfruit = random.choices(availfruits, k=4)
                   print(ansfruit)
                   game = True


