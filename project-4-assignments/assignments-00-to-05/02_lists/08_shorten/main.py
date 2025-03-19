def shorten(lst):
    MAX_LENGTH = 3
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(f"Removed {removed} from the list.")
        
def main():
    user_list = []
    while True:
        try:
         user_input = input("Please enter an element of the list or press enter stop: ")
         if user_input == "":
            break
         user_list.append(user_input)
        except Exception as e:
            print("Error:", e)
    shorten(user_list)
    print(f"The list is now: {user_list}")


if __name__ == "__main__":
    main()
