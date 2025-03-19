#type: ignore
from colorama import Style
def repeat_3_times(message):
    list_before = []
    list_after = []
    print("List before:", list_before)
    for i in range(3):
        list_after.append(message)
    return f"List after: {list_after}"

def main():
    print(Style.BRIGHT)
    input_message = input("Enter a message: ")
    print(Style.RESET_ALL)
    print(repeat_3_times(input_message))


if __name__ == "__main__":
    main()
