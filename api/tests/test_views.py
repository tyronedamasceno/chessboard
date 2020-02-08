from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api.models import ChessPiece

REGISTER_PIECE_URL = reverse('pieces-list')


class ChessboardRegisterPieceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_chess_piece_register_requires_both_type_and_color(self):
        response = self.client.post(REGISTER_PIECE_URL)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type', response.data)
        self.assertIn('color', response.data)

    def test_chess_piece_register_requires_a_valid_type(self):
        payload = {
            'type': 'wrong_type',
            'color': 'white'
        }

        response = self.client.post(REGISTER_PIECE_URL, data=payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type', response.data)

    def test_chess_piece_register_requires_a_valid_color(self):
        payload = {
            'type': 'knight',
            'color': 'wrong_color'
        }

        response = self.client.post(REGISTER_PIECE_URL, data=payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('color', response.data)

    def test_chess_piece_register_successful(self):
        payload = {
            'type': 'knight',
            'color': 'white'
        }

        response = self.client.post(REGISTER_PIECE_URL, data=payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChessPiece.objects.count(), 1)
