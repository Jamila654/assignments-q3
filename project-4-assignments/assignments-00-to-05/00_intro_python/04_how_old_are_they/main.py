def main():
    print("Hello from 04-how-old-are-they!")
    
    anton_age : int = 21
    beth_age : int= 6 + anton_age
    chen_age : int = 20 + beth_age
    drew_age : int = chen_age + anton_age
    ethan_age : int = chen_age
    
    print(f"Anton is {anton_age}\nBeth is {beth_age}\nChen is {chen_age}\nDrew is {drew_age}\nEthan is {ethan_age}")


if __name__ == "__main__":
    main()
