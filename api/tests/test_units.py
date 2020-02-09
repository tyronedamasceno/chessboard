from django.test import TestCase

from api.utils import (
    find_knight_possible_moves, sum_char, calculate_new_letter,
    calculate_new_number, find_knight_possible_moves_in_two_turns
)


class CalculatingNewPositionsTestCase(TestCase):
    def test_sum_char_function(self):
        test_cases = {
            ('A', 1): 'B',
            ('A', 2): 'C',
            ('D', -1): 'C',
            ('D', -2): 'B',
            ('2', 1): '3',
            ('2', 2): '4',
            ('5', -1): '4',
            ('5', -2): '3',
        }

        for input_pair, expected_output in test_cases.items():
            self.assertEqual(sum_char(*input_pair), expected_output)

    def test_calculate_letter_return_None_if_letter_is_out_of_board(self):
        test_cases = [('A', -1), ('B', -2), ('G', 2), ('H', 1)]
        for input_pair in test_cases:
            self.assertIsNone(calculate_new_letter(*input_pair))

    def test_calculate_number_return_None_if_number_is_out_of_board(self):
        test_cases = [('1', -1), ('2', -2), ('7', 2), ('8', 1)]
        for input_pair in test_cases:
            self.assertIsNone(calculate_new_number(*input_pair))


class OneTurnKnightFindPossibleMovementsTestCase(TestCase):
    def test_one_turn_knight_movements_from_center_of_board(self):
        letter = 'D'
        number = '4'
        possibilities = find_knight_possible_moves(letter, number)

        expected = set([
            ('B', '3'), ('B', '5'), ('C', '2'), ('C', '6'),
            ('E', '2'), ('E', '6'), ('F', '3'), ('F', '5'),
        ])

        self.assertEqual(possibilities, expected)

    def test_one_turn_knight_movements_from_edge_of_board(self):
        letter = 'A'
        number = '5'
        possibilities = find_knight_possible_moves(letter, number)

        expected = set([
            ('B', '3'), ('B', '7'), ('C', '4'), ('C', '6'),
        ])

        self.assertEqual(possibilities, expected)

    def test_one_turn_knight_movements_from_corner_of_board(self):
        letter = 'A'
        number = '1'
        possibilities = find_knight_possible_moves(letter, number)

        expected = set([('B', '3'), ('C', '2')])

        self.assertEqual(possibilities, expected)


class TwoTurnsKnightFindPossibleMovementsTestCase(TestCase):
    def test_find_knight_moves_in_two_turns_from_corner_of_board(self):
        letter = 'A'
        number = '1'
        possibilities = find_knight_possible_moves_in_two_turns(letter, number)

        expected = set([
            ('A', '1'), ('A', '3'), ('A', '5'), ('B', '4'), ('C', '1'),
            ('C', '5'), ('D', '2'), ('D', '4'), ('E', '1'), ('E', '3')
        ])

        self.assertEqual(possibilities, expected)

    def test_find_knight_moves_in_two_turns_from_center_of_board(self):
        letter = 'D'
        number = '4'
        possibilities = find_knight_possible_moves_in_two_turns(letter, number)

        expected = set([
            ('A', '1'), ('A', '3'), ('A', '5'), ('A', '7'), ('B', '4'),
            ('B', '8'), ('C', '1'), ('C', '3'), ('C', '5'), ('C', '7'),
            ('D', '2'), ('D', '4'), ('D', '6'), ('D', '8'), ('E', '1'),
            ('E', '3'), ('E', '5'), ('E', '7'), ('F', '4'), ('F', '8'),
            ('G', '1'), ('G', '3'), ('G', '5'), ('G', '7'), ('H', '2'),
            ('H', '4'), ('H', '6')
        ])

        self.assertEqual(possibilities, expected)
