import random
import time
def main():
    print("Hello from 06-rolldice!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Rolling the dice...")
    time.sleep(1)
    print(f"dice1: {dice1}\ndice2: {dice2}\nTotal: {total}")
    
    


if __name__ == "__main__":
    main()
