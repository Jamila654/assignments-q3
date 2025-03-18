#type: ignore
from colorama import Fore, Style
import time
def main():
    print("Hello from 02-emc2!")
    c = 299792458
    try:
        print(Style.BRIGHT)
        m = float(input("Enter mass (kg): "))
        print(Style.RESET_ALL)
        E = m * c**2
        print(f"e = m * C^2...\nm = {m} kg\nC = 299792458 m/s")
        time.sleep(1)
        print(f"{E} joules of energy!")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return


if __name__ == "__main__":
    main()
