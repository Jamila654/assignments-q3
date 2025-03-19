#type: ignore
from colorama import Style
def main():
    fruits = {
        "apple": 1,
        "banana": 2,
        "orange": 3,
        "pear": 4,
        "grape": 5,
        "mango": 6,
        "kiwi": 7,
        "pineapple": 8,
        "coconut": 9,
        "papaya": 10    
    }
    total_price = 0
    for fruit in fruits:
        print(Style.BRIGHT)
        print(f"How many {fruit} do you want to buy?")
        print(Style.RESET_ALL)
        quantity = int(input())
        total_price += quantity * fruits[fruit]
    print(f"Total price: {total_price}")


if __name__ == "__main__":
    main()
