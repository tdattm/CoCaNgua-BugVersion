import pygame
from game.board import Board
from game.pieces import Piece
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
                    elif self.check_piece_blocked(piece, value_dice):
                        pass 
                    else:   
                        walk_moves = self.get_walk_moves(piece, value_dice)
                        if not self.check_piece_at_nest(piece, value_dice) and not self.piece_can_reach_nest(piece, value_dice):
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
    
    # def get_valid_moves(self, piece, value_dice):
    #     if self.can_eat:
    #         self.valid_moves = self.get_eat_moves(piece, value_dice)
    #     else:
    #         self.valid_moves = set.union(self.get_valid_moves(self.selected, value_dice), self.get_eat_moves(self.selected, value_dice))
    
    def get_walk_moves(self, piece, value_dice):
        walk_moves = set([])
        
        position = self.position_piece(piece)
        new_position = -1
        if self.piece_can_reach_nest(piece):
            if piece.color == "red":
                new_position = 55 + (value_dice - 55 + position)/10
            elif piece.color == "blue":
                new_position = 41 + (value_dice - 41 + position)/10
            elif piece.color == "orange":
                new_position = 13 + (value_dice - 13 + position)/10
            else: 
                new_position = 27 + (value_dice - 27 + position)/10
        elif self.check_piece_at_nest(piece):
            if piece.color == "red":
                temp = position + value_dice/10
                if temp > 55.6:
                    pass
                else:
                    new_position = position + value_dice/10
            elif piece.color == "blue":
                temp = position + value_dice/10
                if temp > 41.6:
                    pass
                else:
                    new_position = position + value_dice/10
            elif piece.color == "orange":
                temp = position + value_dice/10
                if temp > 13.6:
                    pass
                else:
                    new_position = position + value_dice/10
            else: 
                temp = position + value_dice/10
                if temp > 27.6:
                    pass
                else:
                    new_position = position + value_dice/10          
        else:
            new_position = position + value_dice
            if new_position > 55:
                new_position = new_position - 55
        
        if new_position != -1:    
            new_position_coord = self.board.position[new_position]
            left_square = self.board.get_piece(new_position_coord[0], new_position_coord[1])
            
            if left_square == 0:
                walk_moves.add(new_position_coord)
            return walk_moves
        else:
            return set([])
    
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
    
    def check_piece_at_nest(self, piece):
        piece_pos = (piece.row, piece.col)
        
        if piece.color == "red":
            nest = [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)]
            for pos in nest:
                if piece_pos == pos:
                    return True
            return False  
        elif piece.color == "blue":
            nest = [(8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9)]
            for pos in nest:
                if piece_pos == pos:
                    return True
            return False
        elif piece_pos == "orange":
            nest = [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]
            for pos in nest:
                if piece_pos == pos:
                    return True
            return False
        else:
            nest = [(14, 7), (13, 7), (12, 7), (11, 7), (10, 7), (9, 7)]
            for pos in nest:
                if piece_pos == pos:
                    return True
            return False
           
    def piece_can_reach_nest(self, piece, value_dice):
        piece_color = piece.color
        position = self.position_piece(piece)
        if piece_color == "red":
            possibles = (50,51,52,53,54,55)
            if position in possibles and position + value_dice > 55:
                return True
            else:
                return False
        elif piece_color == "blue":
            possibles = (36,37,38,39,40,41)
            if position in possibles and position + value_dice > 41:
                return True
            else:
                return False
        elif piece_color == "orange":
            possibles = (8,9,10,11,12,13)
            if position in possibles and position + value_dice > 13:
                return True
            else:
                return False
        else:
            possibles = (22,23,24,25,26,27)
            if position in possibles and position + value_dice > 27:
                return True
            else:
                return False
     
    def check_piece_blocked(self, piece, value_dice):
        pos = self.position_piece(piece)
        end_check = 0
        if piece.color == "red":
            end_check = 55
        elif piece.color == "orange":
            end_check = 13
        elif piece.color == "green":
            end_check = 27
        else:
            end_check = 41
        
        if self.piece_can_reach_nest(piece, value_dice):
            for _ in range(pos + 1, end_check + 1):
                pos_coord = self.board.position[_]
                if self.board.get_piece(pos_coord[0], pos_coord[1]):
                    return True
            
            for i in range(1, value_dice - end_check + pos + 1):
                pos_coord = self.board.position[end_check + i*0.1]
                if self.board.get_piece(pos_coord[0], pos_coord[1]):
                    return True
        elif self.check_piece_at_nest(piece, value_dice):
            if value_dice*0.1 + pos > end_check + 0.6:
                pass
            else:
                for _ in range(1, value_dice + 1):
                    pos_coord = self.board.position[pos + _*0.1]
                    if self.board.get_piece(pos_coord[0], pos_coord[1]):
                        return True
        else:
            for _ in range(pos + 1, pos + value_dice):
                pos_coord = self.board.position[_]
                if self.board.get_piece(pos_coord[0], pos_coord[1]):
                    return True
        return False
     
    def _move(self, row, col):
        new_position = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            if new_position == 0:
                self.board.move(self.selected, row, col)       
                return True
            else:
                if self.can_eat:
                    self.board.board[row][col] = 0
                    self.board.move(self.selected, row, col)
                    return True
        else:
            return False
    