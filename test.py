import unittest
from core.classes import *

# Test class template
'''
class NameTests(unittest.TestCase):
    # Declare some testing variables
    try:
        a = Name()
    except Exception as e:
        print('Failed to create Name: ', e)

    # Tests for creation
    
    # Tests for dunder functions

    # Tests for getters
    
    # Tests for setters
    
    # Tests for external functions
'''

class PieceTests(unittest.TestCase):
    # Declare some testing variables
    try:
        white_pawn = Piece(Piece.WHITE, Piece.PAWN)

        # Ahaha...
        # bishop_black = Piece(Piece.BISHOP, Piece.BLACK)
    except Exception as e:
        print('Uh oh! Failed to create Pieces: ', e)
    
    # Tests for creation
    def test_piece_create_args_count_low(self):
        with self.assertRaises(Exception) as error:
            Piece(Piece.WHITE)
        self.assertRaises(TypeError, error)

    def test_piece_create_args_count_high(self):
        with self.assertRaises(Exception) as error:
            Piece(Piece.WHITE, Piece.PAWN, Piece.KING)
        self.assertRaises(TypeError, error)

    def test_piece_create_wrong_side(self):
        with self.assertRaises(Exception) as error:
            Piece('V', Piece.PAWN)
        self.assertTrue('Side is incorrect.' in str(error.exception))
    
    def test_piece_create_wrong_type(self):
        with self.assertRaises(Exception) as error:
            Piece(Piece.WHITE, 'J')
        self.assertTrue('Type is incorrect.' in str(error.exception))

    # Tests for dunder functions
    def test_piece_str(self):
        self.assertEqual(str(self.white_pawn), 'White pawn')
    
    def test_piece_eq(self):
        self.assertEqual(self.white_pawn, Piece(Piece.WHITE, Piece.PAWN))
    
    def test_piece_ne_side(self):
        self.assertNotEqual(self.white_pawn, Piece(Piece.BLACK, Piece.PAWN))
    
    def test_piece_ne_side(self):
        self.assertNotEqual(self.white_pawn, Piece(Piece.WHITE, Piece.BISHOP))

    # Tests for getters
    def test_piece_get_side(self):
        self.assertEqual(self.white_pawn.get_side(), Piece.WHITE)

    def test_piece_get_type(self):
        self.assertEqual(self.white_pawn.get_type(), Piece.PAWN)
    
    # Tests for setters

    # Tests for external functions

class SquareTests(unittest.TestCase):
    # Declare some testing variables
    try:
        d4 = Square('d4') # Great square
    except Exception as e:
        print('Failed to create Squares: ', e)

    # Tests for creation
    def test_square_create_str(self):
        self.assertEqual(str(self.d4), 'd4')
    
    def test_square_create_piece(self):
        self.assertIsNone(self.d4.get_piece())
    
    def test_square_create_wrong_file(self):
        with self.assertRaises(Exception) as error:
            Square('i1')
        self.assertTrue('File is incorrect.' in str(error.exception))

    def test_square_create_wrong_rank_less(self):
        with self.assertRaises(Exception) as error:
            Square('a0')
        self.assertTrue('Rank is incorrect.' in str(error.exception))
    
    def test_square_create_wrong_rank_more(self):
        with self.assertRaises(Exception) as error:
            Square('a9')
        self.assertTrue('Rank is incorrect.' in str(error.exception))
    
    # Tests for dunder functions
    def test_square_str(self):
        self.assertEqual(str(self.d4), 'd4')
    
    def test_square_eq(self):
        self.assertEqual(self.d4, Square('d4'))

    # Tests for getters
    def test_square_get_file(self):
        self.assertEqual(self.d4.get_file(), 'd')

    def test_square_get_rank(self):
        self.assertEqual(self.d4.get_rank(), 4)
    
    def test_square_get_piece(self):
        self.assertIsNone(self.d4.get_piece())
    
    # Tests for setters
    def test_square_set_piece(self):
        e4 = Square('e4')
        e4.set_piece(Piece(Piece.WHITE, Piece.PAWN))
        self.assertEqual(str(e4.get_piece()), 'White pawn')
    
    # Tests for external functions

class BoardTests(unittest.TestCase):
    # Declare some testing variables
    try:
        board = Board()
    except Exception as e:
        print('Failed to create Boards: ', e)

    # Tests for creation
    # No arguments
    
    # Tests for dunder functions
    def test_board_str(self):
        self.assertTrue('e4, f4, g4, h4, a5, b5, c5, d5' in str(self.board))

    # Tests for getters
    def test_board_get_piece(self):
        self.assertEqual(self.board.get_piece(Square('e1')), Piece(Piece.WHITE, Piece.KING))

    # Tests for setters
    def test_board_set_piece(self):
        temp_board = Board()
        temp_square = Square('e1')

        temp_board.set_piece(temp_square, Piece(Piece.BLACK, Piece.QUEEN))

        self.assertEqual(temp_board.get_piece(temp_square), Piece(Piece.BLACK, Piece.QUEEN))
    
    # Tests for external functions



def ad_hoc_test():
    print('-:[ AD HOC TESTS STARTING ]:-')

    print('-:[  AD HOC TESTS ENDING  ]:-')

if __name__ == '__main__':
    ad_hoc_test()
    unittest.main()