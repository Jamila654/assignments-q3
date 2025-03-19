def main():
    num = 0
    while num < 100:
        try:
            num = int(input("Enter a number: "))
            print(num * 2)
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
