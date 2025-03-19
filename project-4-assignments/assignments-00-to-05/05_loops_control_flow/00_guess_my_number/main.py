import random
def main():
    number = random.randint(0, 99)
    while True:
        print("I am thinking of a number between 0 and 99...")
        guess = int(input("Enter a guess: "))
        if guess == number:
            print("You guessed it!")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    main()
