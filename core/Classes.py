# https://en.wikipedia.org/wiki/Portable_Game_Notation


# Class template
'''
class Name:
    # Constants

    # Dunder functions
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        return str(self)
    
    # Private functions

    # Getters

    # Setters

    # External functions
'''

class Piece:
    # Constants
    WHITE = 'W'
    BLACK = 'B'

    PAWN = 'P'
    KNIGHT = 'N'
    BISHOP = 'B'
    ROOK = 'R'
    QUEEN = 'Q'
    KING = 'K'

    # Dunder functions
    def __init__(self, side, type):
        if not self.__check_side(side):
            raise Exception('Side is incorrect.')
        
        if not self.__check_type(type):
            raise Exception('Type is incorrect.')
        
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

    def __eq__(self, other):
        if self.get_side() == other.get_side() and \
        self.get_type() == other.get_type():
            return True
        return False

    def __ne__(self, other):
        return not self == other
    
    # Private functions
    def __check_side(self, side_input):
        if side_input not in [self.WHITE, self.BLACK]:
            return False
        return True
    
    def __check_type(self, type_input):
        if type_input not in [self.PAWN, self.KNIGHT, \
                              self.BISHOP, self.ROOK, \
                                self.QUEEN, self.KING]:
            return False
        return True
    
    # Getters
    def get_side(self):
        return self.__side
    
    def get_type(self):
        return self.__type
    
    # Setters

    # External functions
    
class Square:
    # Constants
    FILE_ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Dunder functions
    def __init__(self, square_str):
        file, rank = self.__convert_square_str(square_str)
        
        self.__file_index = self.__encode_file(file)
        self.__rank_index = rank - 1 # Keep this as int
        self.__piece = None
    
    def __str__(self):
        return self.get_file() + str(self.get_rank())

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if self.get_file() == other.get_file() and \
            self.get_rank() == other.get_rank():
            return True
    
    def __ne__(self, other):
        return not (self == other)

    # Private functions
    def __check_file(self, file):
        if file not in self.FILE_ARRAY:
            raise Exception('File is incorrect.')
    
    def __check_rank(self, rank):
        if rank < 1 or rank > 8:
            raise Exception('Rank is incorrect.')

    def __convert_square_str(self, square_str):
        if len(square_str) != 2:
            raise Exception('Square is incorrect.')
        self.__check_file(square_str[0])
        self.__check_rank(int(square_str[1]))
        
        return square_str[0], int(square_str[1])

    def __encode_file(self, file):
        return self.FILE_ARRAY.index(file)
    
    def __decode_file(self, file_index):
        return self.FILE_ARRAY[file_index]
    
    # Getters
    def get_file(self):
        return self.__decode_file(self.__file_index)

    def get_rank(self):
        return self.__rank_index + 1
    
    def get_piece(self):
        return self.__piece
    
    # Setters
    def set_piece(self, piece):
        self.__piece = piece
    
    # External functions

class Board:
    # Constants

    # Dunder functions
    def __init__(self):
        self.__board_array = []

        for rank in range(1, 9):
            for file in Square.FILE_ARRAY:
                self.__board_array += [Square(file + str(rank))]
        
        self.__standard_setup()
    
    def __str__(self):
        return str(self.__board_array)

    def __repr__(self):
        str(self)
    
    # Private functions
    def __get_board_square(self, input_square):
        for square in self.__board_array:
            if input_square == square:
                return square

    def __standard_setup(self):
        # Kings
        self.__get_board_square(Square('e1')).set_piece(Piece(Piece.WHITE, Piece.KING))
        self.__get_board_square(Square('e8')).set_piece(Piece(Piece.BLACK, Piece.KING))

    # Getters
    def get_piece(self, square):
        return self.__get_board_square(square).get_piece()

    def set_piece(self, square, piece):
        self.__get_board_square(square).set_piece(piece)

    # Setters

    # External functions