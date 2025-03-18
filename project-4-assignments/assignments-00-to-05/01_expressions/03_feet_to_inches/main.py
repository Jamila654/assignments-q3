def main():
    print("Hello from 03-feet-to-inches!")
    inch_per_foot = 12
    try:
        f = float(input("Enter feet: "))
        i = f * inch_per_foot
        print(f"{f} feet is {i} inches!")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return


if __name__ == "__main__":
    main()
