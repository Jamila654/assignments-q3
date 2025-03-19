#type: ignore
from colorama import Style
def main():
    user_list = []
    i = 1
    while True:
        user_input = input(f"Enter a value: {i}: ")
        if user_input == "":
            break
        user_list.append(user_input)
        i += 1
    print(f"Here's the list: {user_list}")


if __name__ == "__main__":
    main()
