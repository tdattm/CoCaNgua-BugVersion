import pygame
from game.constants import SQUARE_HEIGHT

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    
    def get_position(self):
        self.xCenter = SQUARE_HEIGHT//2 + self.col*SQUARE_HEIGHT
        self.yCenter = SQUARE_HEIGHT//2 + self.row*SQUARE_HEIGHT
        
    def draw_piece(self, window):
        self.get_position()
        pieceRadius = SQUARE_HEIGHT//2.3
        
        pygame.draw.circle(window, self.color, (self.xCenter, self.yCenter), pieceRadius)
        
    def draw_Valid_Moves(self, window, validMoves):
        validMoveRadius = SQUARE_HEIGHT//2.3
        for move in validMoves:
            xMove = move[1]*SQUARE_HEIGHT + SQUARE_HEIGHT//2
            yMove = move[0]*SQUARE_HEIGHT + SQUARE_HEIGHT//2
            pygame.draw.circle(window, (166, 166, 166), (xMove, yMove), validMoveRadius, 2)
        