import unittest
from core.classes import Piece, Board

class PieceTests(unittest.TestCase):
    def test_piece_creation_pawn(self):
        pawn = Piece(Piece.WHITE, Piece.PAWN)
        self.assertEqual(str(pawn), 'White pawn')

    def test_piece_creation_knight(self):
        knight = Piece(Piece.BLACK, Piece.KNIGHT)
        self.assertEqual(str(knight), 'Black knight')

    def test_piece_creation_bishop(self):
        bishop = Piece(Piece.WHITE, Piece.BISHOP)
        self.assertEqual(str(bishop), 'White bishop')

    def test_piece_creation_rook(self):
        rook = Piece(Piece.BLACK, Piece.ROOK)
        self.assertEqual(str(rook), 'Black rook')

    def test_piece_creation_queen(self):
        queen = Piece(Piece.WHITE, Piece.QUEEN)
        self.assertEqual(str(queen), 'White queen')

    def test_piece_creation_king(self):
        king = Piece(Piece.BLACK, Piece.KING)
        self.assertEqual(str(king), 'Black king')

EMPTY_BOARD = '[[None, None, None, None, None, None, None, None], \
    [None, None, None, None, None, None, None, None], \
        [None, None, None, None, None, None, None, None], \
            [None, None, None, None, None, None, None, None], \
                [None, None, None, None, None, None, None, None], \
                    [None, None, None, None, None, None, None, None], \
                        [None, None, None, None, None, None, None, None], \
                            [None, None, None, None, None, None, None, None]]'

class BoardTests(unittest.TestCase):
    def test_empty_board_creation(self):
        self.assertEqual(str(Board()), '[[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]')
    
    def test_white_king_position(self):
        self.assertEqual(Board())

if __name__ == '__main__':
    unittest.main()