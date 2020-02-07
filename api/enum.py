from collections import namedtuple
from enum import Enum

choice = namedtuple('Choice', 'name value')


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [choice(e.name, e.value) for e in cls]


class ChessPieceType(ChoiceEnum):
    king = 'king'
    queen = 'queen'
    rook = 'rook'
    knight = 'knight'
    bishop = 'bishop'
    pawn = 'pawn'


class ChessPieceColor(ChoiceEnum):
    white = 'white'
    black = 'black'
