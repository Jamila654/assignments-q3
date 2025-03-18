import random
import time

sides = 6
def roll_dice():
    dice1 = random.randint(1, sides)
    dice2 = random.randint(1, sides)
    return f"dice1: {dice1}, dice2: {dice2}"
    
def main():
    print("Hello from 01-dicesimulator!")
    time.sleep(1)
    
    for i in range(1,4):
        print(roll_dice())
        time.sleep(1)


if __name__ == "__main__":
    main()
