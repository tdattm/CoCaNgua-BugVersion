import pygame
import sys
from game.game import Game
from button import Button
from game.constants import WIDTH, HEIGHT, ROLL_DICE, SQUARE_HEIGHT

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Cờ cá ngựa 🐴")

def get_row_col_from_mouse(MOUSE_POS):
    x, y = MOUSE_POS
    row = int(y // SQUARE_HEIGHT)
    col = int(x // SQUARE_HEIGHT)
    return row, col
    # print(row, col)

def start_game():
    run = True
    game = Game(window)
    dice_rolled = False
    value_dice = 0
    ROLL_BOTTON = Button(image=ROLL_DICE, pos=(20*SQUARE_HEIGHT, SQUARE_HEIGHT*2.25), text_Input="Roll", font=getFont(1), baseColor="black")
    
    while run:
        
        
        game.board.draw_board(window, game.selected, game.valid_move)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                MOUSE_POS = pygame.mouse.get_pos()
                
                if ROLL_BOTTON.checkForInput(MOUSE_POS):
                    game.dice.value_dice()
                    value_dice = game.dice.get_value_dice()
                    dice_rolled = True
                
                selected_row, selected_col = get_row_col_from_mouse(MOUSE_POS)
                game.select(selected_row, selected_col, value_dice)
                # value_dice = 0
                # if game.winner != None:
                #     run = False                
                
                    
        if dice_rolled:
            game.dice.draw_dice(window)
            
                        
        pygame.display.update()

# def dice_field():
#     game = Game(window)
#     dice_rolled = False
    
#     while True:
#         ROLL_BOTTON = Button(image=ROLL_DICE, pos=(20*SQUARE_HEIGHT, SQUARE_HEIGHT*2.25), text_Input="Roll", font=getFont(1), baseColor="black")
#         MOUSE_POS = pygame.mouse.get_pos()
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: 
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if ROLL_BOTTON.checkForInput(MOUSE_POS):
#                         game.dice.value_dice()
#                         value_dice = game.dice.get_value_dice()
#                         dice_rolled = True

#         if dice_rolled:
#             game.dice.draw_dice(window)
            
                        
#         pygame.display.update()
        
def getFont(size): 
    return pygame.font.Font("assets/font.ttf", size) 

       
start_game()
# get_row_col_from_mouse(pygame.mouse.get_pos())
                
        