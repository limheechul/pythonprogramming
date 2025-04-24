from random import randint

def roll_dice():
    return randint(1,6)

def main():
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())

if __name__ == '__main__':
    main()
