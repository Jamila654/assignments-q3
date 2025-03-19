def main():
    print("Hello from 02-double-list!")
    
    list_numbers = []
    double_list = []
    try:
        while True:
            print("Enter 0 to stop.")
            numbers = float(input("Enter a number: "))
            list_numbers.append(numbers)
            if numbers == 0:
                break
        list_numbers.remove(0)

        for number in list_numbers:
            double = number * 2
            double_list.append(double)
            
        double_list.pop()
        list_numbers.pop()
        print(f"""Original list: {list_numbers}\nDouble list: {double_list}""")
        
    except ValueError:
        pass



if __name__ == "__main__":
    main()
