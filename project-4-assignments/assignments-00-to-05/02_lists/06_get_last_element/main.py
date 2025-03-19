def get_last_element(lst):
    return lst[-1]
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
    last_element = get_last_element(user_list)
    print(f"The last element of the list is: {last_element}")


if __name__ == "__main__":
    main()
