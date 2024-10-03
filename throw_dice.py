import random
import time

def throw_dice():
    print("Dice is throwing!")
    time.sleep(2)
    dice_num = random.randint(1,6)
    print(f"Result: {dice_num}")

throw_dice()