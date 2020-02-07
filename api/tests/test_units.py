from unittest.mock import Mock

from django.test import TestCase

from rest_framework import status

from api.views import RegisterPieceView


class ChessboardRegisterPieceTestCase(TestCase):
    def setUp(self):
        self.request = Mock()
        self.view = RegisterPieceView()

    def test_chess_piece_register_requires_both_type_and_color(self):
        self.request.data = {}

        response = self.view.post(self.request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type', response.data)
        self.assertIn('color', response.data)

    def test_chess_piece_register_requires_a_valid_type(self):
        self.request.data = {
            'type': 'wrong_type',
            'color': 'white'
        }

        response = self.view.post(self.request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type', response.data)

    def test_chess_piece_register_requires_a_valid_color(self):
        self.request.data = {
            'type': 'knight',
            'color': 'wrong_color'
        }

        response = self.view.post(self.request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('color', response.data)

    def test_chess_piece_register_successful(self):
        ...
