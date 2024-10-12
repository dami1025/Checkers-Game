import unittest
from CheckersGame import *

class CheckersGameTest(unittest.TestCase):

    """Represents Unit Tests for the CheckersGame portfolio project"""

    def setUp(self):
        pass


    def test_create_player(self):
        """
        Tests that the create player method will create two different player
        """
        game = Checkers()
        player1 = game.create_player('Ham', 'White')
        player2 = game.create_player('Meat', 'Black')
        self.assertIsNot(player1, player2)

    def test_piece_movement(self):
        """
        Tests that the play game method will return the correct piece being moved
        """
        game = Checkers()
        player1 = game.create_player('Ham', 'White')
        player2 = game.create_player('Meat', 'Black')
        game.play_game('Meat', (5,2), (4,3))
        self.assertEqual(game.get_checkers_details((4,3)), 'Black')

    def test_turn_exchange(self):
        """
        Tests that the play game method will change to the correct turn after each player's round
        """
        game = Checkers()
        player1 = game.create_player('Ham', 'White')
        player2 = game.create_player('Meat', 'Black')
        game.play_game('Meat', (5, 2), (4, 3))
        self.assertIsNot(game.get_turn(), "Black") #Since first turn is Black, second turn will be White

    def test_piece_capture(self):
        """
        Tests that the play game method will return the correct number of piece captured, assuming all the
        moves led to the capture are valid
        """

        game = Checkers()
        player1 = game.create_player('Ham', 'White')
        player2 = game.create_player('Meat', 'Black')

        game.play_game('Meat', (5, 0), (4, 1))
        game.play_game('Ham', (2, 1), (3, 2))
        game.play_game('Meat', (6, 1), (5, 0))
        game.play_game('Ham', (2, 3), (3, 4))
        game.play_game('Meat', (4, 1), (2, 3))
        self.assertEqual(player2.get_captured_pieces_count(), 1)



if __name__ == '__main__':
    unittest.main()