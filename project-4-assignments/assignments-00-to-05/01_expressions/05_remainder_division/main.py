#type: ignore
from colorama import Style
def main():
    print("Hello from 05-remainder-division!")
    try:
        print(Style.BRIGHT)
        divided = float(input("Please enter an integer to be divided: "))
        divede_by = float(input("Please enter an integer to divide by: "))
        print(Style.RESET_ALL)
        result = divided // divede_by
        remainder = divided % divede_by
        print(f"The result of this division is {result} with a remainder of {remainder}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return


if __name__ == "__main__":
    main()
