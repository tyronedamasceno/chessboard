POSSIBLE_LETTERS = 'ABCDEFGH'
POSSIBLE_NUMBERS = '12345678'


def sum_char(char, value):
    return chr(ord(char) + value)


def calculate_new_letter(letter, sum_letter):
    new_letter = sum_char(letter, sum_letter)
    if new_letter in POSSIBLE_LETTERS:
        return new_letter


def calculate_new_number(number, sum_number):
    new_number = sum_char(number, sum_number)
    if new_number in POSSIBLE_NUMBERS:
        return new_number


def find_knight_possible_moves(letter, number):
    possibilities = set()
    for value_x in (-2, 2):
        for value_y in (-1, 1):
            new_letter = calculate_new_letter(letter, value_x)
            new_number = calculate_new_number(number, value_y)

            if new_letter and new_number:
                possibilities.add((new_letter, new_number))

    for value_y in (-2, 2):
        for value_x in (-1, 1):
            new_letter = calculate_new_letter(letter, value_x)
            new_number = calculate_new_number(number, value_y)

            if new_letter and new_number:
                possibilities.add((new_letter, new_number))

    return possibilities


def find_knight_possible_moves_in_two_turns(letter, number):
    first_turn_knight_moves = find_knight_possible_moves(letter, number)

    all_second_turn_possibilities = set()

    for letter, number in first_turn_knight_moves:
        second_turn_moves = find_knight_possible_moves(letter, number)
        all_second_turn_possibilities.update(second_turn_moves)

    return all_second_turn_possibilities
