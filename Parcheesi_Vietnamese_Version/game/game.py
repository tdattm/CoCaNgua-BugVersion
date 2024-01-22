import pygame
from game.board import Board
from game.dice import Dice
from game.constants import NROWS, NCOLS

class Game:
    def __init__(self, window):
        self.window = window
        self.board = Board()
        self.dice = Dice()
        self.turn = "red"
        self.selected = None
        self.valid_pieces = set([])
        self.valid_moves = set([])
        self.eating = False
        self.can_eat = False
        self.winner = None
        
    def change_turn(self):
        if self.turn == "red":
            self.turn = "blue"
        elif self.turn == "blue":
            self.turn = "green"
        elif self.turn == "green":
            self.turn = "orange"
        else:
            self.turn = "red"
        self.selected = None
        self.valid_pieces = set([])    
        self.eating = False
        
    def get_valid_pieces(self, value_dice):
        eat_pieces = set([])
        valid_pieces = set([])
        for row in range(NROWS):
            for col in range(NCOLS):
                piece = self.board.get_piece(row, col)
                if piece and piece.color == self.turn:
                    if self.check_piece_at_home(piece):
                        pass
                    else:
                        if self.piece_can_reach_nest(piece):
                            # Continue
                            pass
                        else:     
                            walk_moves = self.get_walk_moves(piece, value_dice)
                            eat_moves = self.get_eat_moves(piece, value_dice)
                            valid_moves = set.union(walk_moves, eat_moves)
                            if eat_moves != set([]):
                                eat_pieces.add(piece)
                            elif valid_moves != set([]):
                                valid_pieces.add(piece)
                            else:
                                pass
        if eat_pieces != set([]):
            self.can_eat = True
        else:
            self.can_eat = False
        return valid_pieces
    
    def get_valid_moves(self, piece, value_dice):
        if self.can_eat:
            self.valid_moves = self.get_eat_moves(piece, value_dice)
        else:
            self.valid_moves = set.union(self.get_valid_moves(self.selected, value_dice), self.get_eat_moves(self.selected, value_dice))
    
    def get_walk_moves(self, piece, value_dice):
        walk_moves = set([])
        
        position = self.position_piece(piece)
        new_position = position + value_dice
        if new_position > 55:
            new_position = new_position - 55
            
        new_position_coord =  self.board.position[new_position]
        left_square = self.board.get_piece(new_position_coord[0], new_position_coord[1])
        
        if left_square == 0:
            walk_moves.add(new_position_coord)
        return walk_moves
    
    def get_eat_moves(self, piece, value_dice):
        eat_moves = set([])
        
        position = self.position_piece(piece)
        new_position = position + value_dice
        if new_position > 55:
            new_position = new_position - 55
            
        new_position_coord =  self.board.position[new_position]
        left_piece = self.board.get_piece(new_position_coord[0], new_position_coord[1])
        
        if left_piece == 0:
            pass
        elif left_piece.color == self.turn:
            pass
        else:
            eat_moves.add(new_position_coord)
        return eat_moves
           
    def position_piece(self, piece):
        pos = (piece.row, piece.col)
        
        for key, value in self.board.position.items():
            if value == pos:
                return key
         
    def check_piece_at_home(self, piece):
        # coordinates of home's piece
        home = [(2, 2), (2, 3), (3, 2), (3, 3), (2, 12), (2, 13), (3, 12), (3, 13),\
             (12, 2), (12, 3), (13, 2), (13, 3), (12, 12), (12, 13), (13, 12), (13, 13)]
        
        piece_pos = (piece.row, piece.col)
        for pos in home:
            if piece_pos == pos:
                return True
        return False
           
    def piece_can_reach_nest(self, piece, value_dice):
        piece_color = piece.color
        position = self.position_piece(piece)
        if piece_color == "red":
            possibles = (50,51,52,53,54,55)
            if position in possibles:
                return True
            else:
                return False
        elif piece_color == "blue":
            possibles = (36,37,38,39,40,41)
            if position in possibles:
                return True
            else:
                return False
        elif piece_color == "orange":
            possibles = (8,9,10,11,12,13)
            if position in possibles:
                return True
            else:
                return False
        else:
            possibles = (22,23,24,25,26,27)
            if position in possibles:
                return True
            else:
                return False
     
    def _move(self, row, col):
        new_position = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            if new_position == 0:
                self.board.move(self.selected, row, col)       
                return True
            else:
                if self.can_eat:
                    slain_color = self.board.board[row][col].color
                    new_position = 0
                    self.board.reduce_piece(slain_color)
                    self.board.move(self.selected, row, col)
                    return True
        else:
            return False        
    