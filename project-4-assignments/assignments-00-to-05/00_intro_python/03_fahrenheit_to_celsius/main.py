#type: ignore
from colorama import Style
def main():
    print("Hello from 03-fahrenheit-to-celsius!")
    print(Style.BRIGHT)
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        print(Style.RESET_ALL)
        degrees_celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"Temperature: {fahrenheit}F = {degrees_celsius}C.")
    except Exception as e:
        print("Exception occurred: ", e)


if __name__ == "__main__":
    main()
