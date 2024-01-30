import random
from game.constants import SQUARE_HEIGHT, DICE_1, DICE_2, DICE_3, DICE_4, DICE_5, DICE_6

class Dice:
    def __init__(self):
        self.dice = 0
        self.value_dice()
    
    def value_dice(self):
        self.dice = random.randint(1, 6)
    
    def draw_dice(self, window):
        dice_img = [DICE_1, DICE_2, DICE_3, DICE_4, DICE_5, DICE_6]

        # PRINT DICE
        for j in range(len(dice_img)):
            if j == self.dice-1:
                window.blit(dice_img[j], (SQUARE_HEIGHT*19, SQUARE_HEIGHT*8))


    def get_value_dice(self):
        return self.dice