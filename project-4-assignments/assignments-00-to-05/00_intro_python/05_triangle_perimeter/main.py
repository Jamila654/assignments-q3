#type: ignore
from colorama import Style
def main():
    print("Hello from 05-triangle-perimeter!")
    
    try:
        print(Style.BRIGHT)
        side1 = float(input("What is the length of side 1? "))
        side2 = float(input("What is the length of side 2? "))
        side3 = float(input("What is the length of side 3? "))
        print(Style.RESET_ALL)
        perimeter = side1 + side2 + side3
        print(f"The perimeter of the triangle is {perimeter}")
    except Exception as e:
        print("Exception occurred: ", e)


if __name__ == "__main__":
    main()
