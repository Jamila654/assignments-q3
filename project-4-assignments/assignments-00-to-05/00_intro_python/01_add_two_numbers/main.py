def main():
    print("This function adds two numbers")
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)
    except Exception as e:
        print("Exception occurred: ", e)


if __name__ == "__main__":
    main()
