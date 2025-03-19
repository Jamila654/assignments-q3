def main():
    MAX_NUMBER: int = 100
    num = 0
    while num <= MAX_NUMBER:
        try:
            num = int(input("Enter a number: "))
            print(num * 2)
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
