#type: ignore
import math
from colorama import Style
def main():
    print("Hello from 04-pythagorean-theorem!")
    
    try:
        print(Style.BRIGHT)
        a = float(input("Enter the length of AB: "))
        b = float(input("Enter the length of AC: "))
        print(Style.RESET_ALL)
        c = math.sqrt(a**2 + b**2)
        print(f"The length of BC (the hypotenuse) is: {c}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    


if __name__ == "__main__":
    main()
