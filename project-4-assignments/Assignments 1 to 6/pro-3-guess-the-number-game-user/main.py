#type:ignore
import random
import time
import colorama
from colorama import Fore, Style
def guess_the_number():
  user_name = input("\n\t\tEnter your name: ")
  print(Fore.BLUE + f"\n\t\tWelcome to Guess the Number Game {user_name}❕❕\n" + Style.BRIGHT)
  print(Fore.WHITE + Style.BRIGHT)
  random_number = random.randint(1, 100)
  total_guess = 4
  while(total_guess <=4):
    try:
      user_generated_number = int(input("Enter a number between 1 and 100 🔢: "))
      if(user_generated_number <1 or user_generated_number >100):
       print(Fore.RED + "\nPlease enter a number between 1 and 100 only ❌\n" + Style.BRIGHT)
       print(Fore.WHITE + Style.BRIGHT)
       continue
    except ValueError:
      print(Fore.RED + "\nInvalid input! Please enter a number between 1 and 100 ❌\n" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
      continue
    time.sleep(2)
    if(user_generated_number < random_number):
      print(Fore.CYAN + f"\nYour number: {user_generated_number} is less than the random number 🤣" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
    elif(user_generated_number > random_number):
      print(Fore.CYAN + f"\nYour number: {user_generated_number} is greater than the random number 😁" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
    else:
      print(Fore.GREEN + f"\nYour number: {user_generated_number} is equal to the random number: {random_number}!" + Style.BRIGHT)
      print(Fore.GREEN + "You won the game 🙌" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
      break
    if(total_guess == 0):
      print(Fore.RED + "\nYou have run out of attempts!" + Style.BRIGHT)
      print(Fore.RED + "You lost the game 😔" + Style.BRIGHT)
      print(Fore.RED + f"The correct number is {random_number}" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
      play_again = input("Do you want to play again? (y/n): ")
      if(play_again.lower() == "y"):
        guess_the_number()
      else:
        print(Fore.GREEN + "\nThanks for playing 😉!" + Style.BRIGHT)
        print(Fore.WHITE + Style.BRIGHT)
        break
      break
    elif(total_guess == 1):
      print(Fore.CYAN + "1 attempt remaining 😱\n" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
    else:
      print(Fore.CYAN + f"{total_guess} attempts remaining\n" + Style.BRIGHT)
      print(Fore.WHITE + Style.BRIGHT)
    total_guess -=1

guess_the_number()