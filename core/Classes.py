# https://en.wikipedia.org/wiki/Portable_Game_Notation

class Piece:
    WHITE = 'W'
    BLACK = 'B'

    PAWN = 'P'
    KNIGHT = 'N'
    BISHOP = 'B'
    ROOK = 'R'
    QUEEN = 'Q'
    KING = 'K'

    def __init__(self, side, type):
        self.__side = side
        self.__type = type

    def __str__(self):
        side_str = ''
        if self.__side == self.WHITE:
            side_str = 'White'
        elif self.__side == self.BLACK:
            side_str = 'Black'
        else:
            return None

        if self.__type == self.PAWN:
            return side_str + ' pawn'
        elif self.__type == self.KNIGHT:
            return side_str + ' knight'
        elif self.__type == self.BISHOP:
           return side_str + ' bishop'
        elif self.__type == self.ROOK:
            return side_str + ' rook'
        elif self.__type == self.QUEEN:
            return side_str + ' queen'
        elif self.__type == self.KING:
            return side_str + ' king'
        else:
            return None

    def __repr__(self):
        return str(self)
    
class Square:
    def __init__(self):
        pass


class Board:
    def __init__(self):
        self.__board_array = []
        for i in range(8):
            temp_array = []
            for j in range(8):
                temp_array += [None]
            self.__board_array += [temp_array]
    
    def __str__(self):
        return str(self.__board_array)

    def __repr__(self):
        str(self)
    
    def get_piece(self, square):
        pass
    
    def file_index(self, file):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(file)

    def rank_index(self, rank):
        # Probably don't need self, but it's consistent?
        return rank - 1

    def standard_setup(self):
        # Add kings
        self.__board_array[self.rank_index(1)][self.file_index('e')] = \
            Piece(Piece.WHITE, Piece.KING)
        self.__board_array[self.rank_index(8)][self.file_index('e')] = \
            Piece(Piece.BLACK, Piece.KING)