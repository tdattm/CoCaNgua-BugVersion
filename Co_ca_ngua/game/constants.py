import pygame

screen = pygame.display.set_mode()
width_screen, height_screen = screen.get_size()
STANDARD_SIZE = height_screen//9*8

WIDTH, HEIGHT = STANDARD_SIZE + STANDARD_SIZE*8/16, STANDARD_SIZE
NROWS, NCOLS = 16, 16
SQUARE_HEIGHT = HEIGHT/NCOLS

CENTER_SQUARE = pygame.image.load("assets/center_square.png")
STANDARD_CENTER_SQUARE = pygame.transform.scale(CENTER_SQUARE, (SQUARE_HEIGHT*2*0.8, SQUARE_HEIGHT*2*0.8))

BACKGROUND_DICE = pygame.image.load("assets/background_dice.png")
STANDARD_BACKGROUND_DICE = pygame.transform.scale(BACKGROUND_DICE, (SQUARE_HEIGHT*8, SQUARE_HEIGHT*16))
ROLL_DICE = pygame.image.load("assets/roll.png")
ROLL_DICE = pygame.transform.scale(ROLL_DICE, (SQUARE_HEIGHT*5, SQUARE_HEIGHT*3.5))
BOX_DICE = pygame.image.load("assets/dice_box.png")
BOX_DICE = pygame.transform.scale(BOX_DICE, (SQUARE_HEIGHT*5, SQUARE_HEIGHT*5.5))

dice_1 = pygame.image.load("assets/dice_1.png")
dice_2 = pygame.image.load("assets/dice_2.png")
dice_3 = pygame.image.load("assets/dice_3.png")
dice_4 = pygame.image.load("assets/dice_4.png")
dice_5 = pygame.image.load("assets/dice_5.png")
dice_6 = pygame.image.load("assets/dice_6.png")

DICE_1 = pygame.transform.scale(dice_1, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))
DICE_2 = pygame.transform.scale(dice_2, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))
DICE_3 = pygame.transform.scale(dice_3, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))
DICE_4 = pygame.transform.scale(dice_4, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))
DICE_5 = pygame.transform.scale(dice_5, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))
DICE_6 = pygame.transform.scale(dice_6, (SQUARE_HEIGHT*2, SQUARE_HEIGHT*2))