def main():
    try:
        list_numbers = []
        sum = 0
        while True:
            print("Enter 0 to stop.")
            numbers = float(input("Enter number one by one: "))
            list_numbers.append(numbers)
            if numbers == 0:
                break

        for number in list_numbers:
            sum += number
        print("Sum: ", sum)
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
