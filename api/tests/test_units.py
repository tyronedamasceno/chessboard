from django.test import TestCase

from api.utils import find_knight_moves


class KnightMovementsTestCase(TestCase):
    def test_one_round_knight_movements_from_center_of_board(self):
        letter = 'D'
        number = '4'
        possibilities = find_knight_moves(letter, number)
        possibilities = set(possibilities)

        expected = set([
            ('B', '3'), ('B', '5'), ('C', '2'), ('C', '6'),
            ('E', '2'), ('E', '6'), ('F', '3'), ('F', '5'),
        ])

        self.assertEqual(possibilities, expected)

    def test_one_round_knight_movements_from_edge_of_board(self):
        letter = 'A'
        number = '5'
        possibilities = find_knight_moves(letter, number)
        possibilities = set(possibilities)

        expected = set([
            ('B', '3'), ('B', '7'), ('C', '4'), ('C', '6'),
        ])

        self.assertEqual(possibilities, expected)

    def test_one_round_knight_movements_from_corner_of_board(self):
        letter = 'A'
        number = '1'
        possibilities = find_knight_moves(letter, number)
        possibilities = set(possibilities)

        expected = set([('B', '3'), ('C', '2')])

        self.assertEqual(possibilities, expected)
