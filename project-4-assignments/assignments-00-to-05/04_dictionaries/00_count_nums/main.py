#type: ignore
from colorama import Fore
def main():
    user_numbers = []
    while True:
        try:
            print(Fore.BLUE)
            user_number = int(input("Enter a number: "))
            print(Fore.RESET)
            user_numbers.append(user_number)
        except ValueError:
            break
    user_dict = {}
    for number in user_numbers:
        if number in user_dict:
            user_dict[number] += 1
        else:
            user_dict[number] = 1
    for number, count in user_dict.items():
        print(f"{number} appears {count} times")


if __name__ == "__main__":
    main()
