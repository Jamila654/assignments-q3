#type: ignore
from colorama import Fore
def main():
    Peturksbouipo = 16
    Stanlau = 25
    Mayengua = 48
    print(Fore.BLUE)
    user_input = int(input("How old are you? "))
    print(Fore.RESET)
    if user_input >= Peturksbouipo:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")

    if user_input >= Stanlau:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")

    if user_input >= Mayengua:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")


if __name__ == "__main__":
    main()
