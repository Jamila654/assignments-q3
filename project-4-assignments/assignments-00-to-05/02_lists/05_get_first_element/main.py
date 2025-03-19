
def get_first_element(lst):
    return lst[0]
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
    first_element = get_first_element(user_list)
    print(f"The first element of the list is: {first_element}")


if __name__ == "__main__":
    main()
