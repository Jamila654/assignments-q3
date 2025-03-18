#type: ignore
from colorama import Style
def main():
    print("Hello from 06-square-number!")
    
    try:
        print(Style.BRIGHT)
        square_number = float(input("Type a number to see its square: "))
        print(Style.RESET_ALL)
        print(f'{square_number} squared is ', square_number**2)
    except Exception as e:
        print("Exception occurred: ", e)


if __name__ == "__main__":
    main()
