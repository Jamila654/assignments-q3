#type: ignore
import random
import time
import colorama
from colorama import Fore, Style
def guess_the_number():
  print(Fore.BLUE + "\n\t\tWelcome to Guess the Number Game(computer)!\n" + Style.BRIGHT)
  random_number = random.randint(1, 100)
  total_guess = 4
  while(total_guess <=4):
    computer_generated_number = random.randint(1, 100)
    time.sleep(3)
    if(computer_generated_number < random_number):
      print(Fore.CYAN + f"Computer generated number: {computer_generated_number} is less than the random number" + Style.BRIGHT)
    elif(computer_generated_number > random_number):
      print(Fore.CYAN + f"Computer generated number: {computer_generated_number} is greater than the random number" + Style.BRIGHT)
    else:
      print(Fore.GREEN + f"Computer generated number: {computer_generated_number} is equal to the random number: {random_number}!" + Style.BRIGHT)
      print(Fore.GREEN + "Computer won the game" + Style.BRIGHT)
      break
    if(total_guess == 0):
      print(Fore.RED + "\nComputer has run out of attempts!" + Style.BRIGHT)
      print(Fore.RED + "Computer lost the game" + Style.BRIGHT)
      print(Fore.RED + f"The correct number is {random_number}" + Style.BRIGHT)
      break
    elif(total_guess == 1):
      print(Fore.CYAN + "1 attempt remaining\n" + Style.BRIGHT)
    else:
      print(f"{total_guess} attempts remaining\n")
    total_guess -=1

guess_the_number()
