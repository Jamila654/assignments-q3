def main():
    phonebook = {}
    while True:
        try:
            name = input("Enter name: ")
            if name == "":
                break
            number = int(input("Enter number: "))
            if number < 0:
                raise Exception("Number must be positive")
            if name in phonebook:
                raise Exception("Name already exists")
            phonebook[name] = number
        except Exception as e:
            print(e)
            break
    for name, number in phonebook.items():
        print(f"{name}: {number}")


if __name__ == "__main__":
    main()
