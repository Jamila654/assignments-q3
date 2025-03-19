def main():
    MINIMUM_HEIGHT = 52
    while True:
        height = int(input("Enter your height in cm: "))
        if height <= 0:
            print("Please enter a valid height")
            continue
        if height >= MINIMUM_HEIGHT:
            print("You are tall enough to ride")
            break
        else:
            print("You are not tall enough to ride")


if __name__ == "__main__":
    main()
