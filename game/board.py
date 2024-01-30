import pygame
from game.pieces import Piece
from game.constants import SQUARE_HEIGHT, NROWS, NCOLS, STANDARD_CENTER_SQUARE, STANDARD_BACKGROUND_DICE, ROLL_DICE, BOX_DICE

class Board:
    def __init__(self):
        self.board = []
        self.initialize_board()
        self.position = {
                        0: (0, 6), 1: (1, 6), 2: (2, 6), 3: (3, 6), 4: (4, 6), 5: (5, 6), 6: (6, 6),
                        7: (6, 5), 8: (6, 4), 9: (6, 3), 10: (6, 2), 11: (6, 1), 12: (6, 0), 13: (7, 0),
                        13.1: (7, 1), 13.2: (7, 2), 13.3: (7, 3), 13.4: (7, 4), 13.5: (7, 5), 13.6: (7, 6),
                        
                        14: (9, 0), 15: (9, 1), 16: (9, 2), 17: (9, 3), 18: (9, 4), 19: (9, 5), 20: (9, 6),
                        21: (10, 6), 22: (11, 6), 23: (12, 6), 24: (13, 6), 25: (14, 6), 26: (15, 6), 27: (15, 7),
                        27.1: (14, 7), 27.2: (13, 7), 27.3: (12, 7), 27.4: (11, 7), 27.5: (10, 7), 27.6: (9, 7),
                        
                        28: (15, 9), 29: (14, 9), 30: (13, 9), 31: (12, 9), 32: (11, 9), 33: (10, 9), 
                        34: (9, 9), 35: (9, 10), 36: (9, 11), 37: (9, 12), 38: (9, 13), 39: (9, 14), 40: (9, 15), 41: (8, 15),  
                        41.1: (8, 14), 41.2: (8, 13), 41.3: (8, 12), 41.4: (8, 11), 41.5: (8, 10), 41.6: (8, 9),  
                        
                        42: (7, 15), 43: (7, 14), 44: (7, 13), 45: (7, 12), 46: (7, 11), 47: (7, 10), 48: (7, 9),
                        49: (5, 9), 50: (4, 9), 51: (3, 9), 52: (2, 9), 53: (1, 9), 54: (0, 9), 55: (0, 8),
                        55.1: (1, 8), 55.2: (2, 8), 55.3: (3, 8), 55.4: (4, 8), 55.5: (5, 8), 55.6: (6, 8),
                        }
        
    def initialize_board(self):
        for row in range(NROWS):
            self.board.append([])
            for col in range(NCOLS):
                if row == 2 or row == 3:
                    if col == 2 or col == 3:
                        self.board[row].append(Piece(row, col, "red"))
                    elif col == 12 or col == 13:
                        self.board[row].append(Piece(row, col, "blue"))
                    else:
                        self.board[row].append(0) 
                elif row == 12 or row == 13:
                    if col == 2 or col == 3:
                        self.board[row].append(Piece(row, col, "orange"))
                    elif col == 12 or col == 13:
                        self.board[row].append(Piece(row, col, "green"))
                    else:
                        self.board[row].append(0) 
                else:
                    self.board[row].append(0) 
    
    def draw_home_and_nest(self, window):
        window.fill((154, 208, 194))
        
        # draw the home paths
        for i in range(0, 14):
            if i<7:
                pygame.draw.rect(window, (154, 59, 59), [SQUARE_HEIGHT*7, SQUARE_HEIGHT + SQUARE_HEIGHT*i, SQUARE_HEIGHT*2, SQUARE_HEIGHT])
            else:
                pygame.draw.rect(window, (199, 220, 167), [SQUARE_HEIGHT*7, SQUARE_HEIGHT + SQUARE_HEIGHT*i, SQUARE_HEIGHT*2, SQUARE_HEIGHT])
             
            if i<7:   
                pygame.draw.rect(window, (192, 130, 97), [SQUARE_HEIGHT + SQUARE_HEIGHT*i, SQUARE_HEIGHT*7, SQUARE_HEIGHT, SQUARE_HEIGHT*2])
            else:
                pygame.draw.rect(window, (79, 112, 156), [SQUARE_HEIGHT + SQUARE_HEIGHT*i, SQUARE_HEIGHT*7, SQUARE_HEIGHT, SQUARE_HEIGHT*2])
            
            
        # make the square on the board
        for col in range(0, 16):
            for row in range(0, 16):
                if col == 7:
                    pygame.draw.rect(window, "black", [col*SQUARE_HEIGHT, row*SQUARE_HEIGHT, SQUARE_HEIGHT*2, SQUARE_HEIGHT], 1)
                elif row == 7:
                    pygame.draw.rect(window, "black", [col*SQUARE_HEIGHT, row*SQUARE_HEIGHT, SQUARE_HEIGHT, SQUARE_HEIGHT*2], 1)
                elif col == 8:
                    pass
                elif row == 8:
                    pass
                else:
                    pygame.draw.rect(window, "black", [col*SQUARE_HEIGHT, row*SQUARE_HEIGHT, SQUARE_HEIGHT, SQUARE_HEIGHT], 1) 
        
        # draw the nest of red pieces
        pygame.draw.rect(window, "red", [0, 0, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6])
        pygame.draw.rect(window, "black", [0, 0, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6], 1)
        pygame.draw.circle(window, (253, 247, 228), [SQUARE_HEIGHT*3, SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2)
        pygame.draw.circle(window, "black", [SQUARE_HEIGHT*3, SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2, 2)
        
        # draw the nest of blue pieces
        pygame.draw.rect(window, "blue", [SQUARE_HEIGHT*10, 0, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6])
        pygame.draw.rect(window, "black", [SQUARE_HEIGHT*10, 0, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6], 1)
        pygame.draw.circle(window, (253, 247, 228), [SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3, SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2)
        pygame.draw.circle(window, "black", [SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3, SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2, 2)
        
        # draw the nest of orange pieces
        pygame.draw.rect(window, "orange", [0, SQUARE_HEIGHT*10, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6])
        pygame.draw.rect(window, "black", [0, SQUARE_HEIGHT*10, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6], 1)
        pygame.draw.circle(window, (253, 247, 228), [SQUARE_HEIGHT*3, SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2)
        pygame.draw.circle(window, "black", [SQUARE_HEIGHT*3, SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2, 2)
        
        # draw the nest of green pieces
        pygame.draw.rect(window, "green", [SQUARE_HEIGHT*10, SQUARE_HEIGHT*10, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6])
        pygame.draw.rect(window, "black", [SQUARE_HEIGHT*10, SQUARE_HEIGHT*10, SQUARE_HEIGHT*6, SQUARE_HEIGHT*6], 1)
        pygame.draw.circle(window, (253, 247, 228), [SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3, SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2)
        pygame.draw.circle(window, "black", [SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3, SQUARE_HEIGHT*10 + SQUARE_HEIGHT*3], SQUARE_HEIGHT*6/2.2, 2)
        
        # draw the center square
        pygame.draw.rect(window, "white", [SQUARE_HEIGHT*7, SQUARE_HEIGHT*7, SQUARE_HEIGHT*2, SQUARE_HEIGHT*2])
        pygame.draw.rect(window, (127,127,127), [SQUARE_HEIGHT*7, SQUARE_HEIGHT*7, SQUARE_HEIGHT*2, SQUARE_HEIGHT*2], 2)
        window.blit(STANDARD_CENTER_SQUARE, (SQUARE_HEIGHT*7 + SQUARE_HEIGHT*0.2, SQUARE_HEIGHT*7 + SQUARE_HEIGHT*0.2))
        
        # draw the roll_dice image
        window.blit(STANDARD_BACKGROUND_DICE, (SQUARE_HEIGHT*16, 0))
        window.blit(ROLL_DICE,(SQUARE_HEIGHT*17.5, SQUARE_HEIGHT*1))
        window.blit(BOX_DICE, (SQUARE_HEIGHT*17.5, SQUARE_HEIGHT*6.5))
                            
    def draw_board(self, window, selected, valid_move):
        self.draw_home_and_nest(window)
        for row in range(NROWS):
            for col in range(NCOLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(window)
        if selected != None:
            selected.draw_Valid_Moves(window, valid_move)
        
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def move(self, piece, row, col):
        # red_home_coords = [(2,2),(2,3),(3,2),(3,3)]
        # blue_home_coords = [(2,12), (2,13), (3,12), (3,13)]
        # orange_home_coords = [(12,2), (12,3), (13,2), (13,3)]
        # green_home_coords = [(12,12), (12,13), (13,12), (13,13)]
        
        captured_piece = self.board[row][col]
        if captured_piece:
            if captured_piece.color == "red":
                for i in (2,3):
                    for j in (2,3):
                        if self.board[i][j] == 0:
                            self.board[i][j] = captured_piece
            elif captured_piece.color == "blue":
                for i in (2,3):
                    for j in (12,13):
                        if self.board[i][j] == 0:
                            self.board[i][j] = captured_piece
            elif captured_piece.color == "orange":
                for i in (12,13):
                    for j in (2,3):
                        if self.board[i][j] == 0:
                            self.board[i][j] = captured_piece
            else:
                for i in (12,13):
                    for j in (12,13):
                        if self.board[i][j] == 0:
                            self.board[i][j] = captured_piece
        else:
            pass

        
        self.board[row][col] = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = 0
        piece.row = row
        piece.col = col
            