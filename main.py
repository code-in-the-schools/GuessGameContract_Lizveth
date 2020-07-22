#random num
import random
num= random.randrange(-100,100)

found = False

while found == False:

  guess = int(import ("Guess of a number: "))
  if(num == guess):
    found== True
    print("You Won!!!")

  elif (guess>num):
    print(str(guess), "is more than it")
  elif (guess<num):
    print(str(guess), " is less than it")
  else:
    print("Wrong! Try again")