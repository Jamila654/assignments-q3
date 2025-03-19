#type:ignore
from colorama import Fore, Style
import time
def countdown_timer():
  print(Fore.BLUE + "\n\t\tWelcome to countdown timer" + Style.BRIGHT)
  print(Fore.RESET)
  try:
    time.sleep(1)
    input_time = int(input("Enter the time in seconds: "))
    while input_time:
      mins, secs = divmod(input_time, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      
      print("\n⏳ " + timer)
      time.sleep(1)
      input_time -=1
      if input_time == 0:
        print("\nTime's up")
        break
  except ValueError:
    print("Invalid input")
countdown_timer()