# https://en.wikipedia.org/wiki/Portable_Game_Notation

class Piece:
    def __init__(self):
        self.__type = ''

    def __str__(self):
        if self.__type == 'P':
            return 'Pawn'
        elif self.__type == 'N':
            return 'Knight'
        elif self.__type == 'B':
            return 'Bishop'
        elif self.__type == 'R':
            return 'Rook'
        elif self.__type == 'Q':
            return 'Queen'
        elif self.__type == 'K':
            return 'King'
        else:
            return None

    def __repr__(self):
        pass