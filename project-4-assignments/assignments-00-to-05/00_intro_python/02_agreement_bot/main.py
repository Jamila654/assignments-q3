#type: ignore
from colorama import Style
def main():
    print("Agreement bot")
    
    try:
        print(Style.BRIGHT)
        user_fav_animal =input("What is your favorite animal? ")
        print(Style.RESET_ALL)
        if user_fav_animal.isdigit():
            print("That is not an animal!")
        else:
            print(f'My favorite animal is also {user_fav_animal}!')
    except Exception as e:
        print("Exception occurred: ", e)


if __name__ == "__main__":
    main()
