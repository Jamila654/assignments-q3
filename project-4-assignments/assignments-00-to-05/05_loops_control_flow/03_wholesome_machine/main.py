#type: ignore
from colorama import Fore, Back, Style
def main():
    AFFIRMATION : str = "I am capable of doing anything I put my mind to."
    print("Please type the following affirmation: " + AFFIRMATION)
    while True:
        print(Fore.BLUE)
        user_input : str = input()
        if user_input == AFFIRMATION:
            print(Fore.RESET)
            print("Correct!")
            break
        else:
            print(Fore.RESET)
            print("Incorrect, please try again.")


if __name__ == "__main__":
    main()
