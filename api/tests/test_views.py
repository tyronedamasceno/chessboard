import uuid

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api.models import ChessPiece

REGISTER_PIECE_URL = reverse('pieces')


class ChessboardRegisterPieceTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ChessboardRegisterPieceTestCase, cls).setUpClass()
        cls.client = APIClient()

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


class ChessBoardSetPiecePositionTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ChessBoardSetPiecePositionTestCase, cls).setUpClass()
        cls.client = APIClient()
        cls.default_piece = ChessPiece.objects.create(
            type='knight', color='white'
        )
        cls.default_url = reverse('set-position', args=[cls.default_piece.id])

    def test_set_piece_requires_valid_piece_id_and_AN_position(self):
        response = self.client.post(self.default_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('letter', response.data)
        self.assertIn('number', response.data)

    def test_set_piece_with_invalid_piece_id_returns_404(self):
        wrong_id = uuid.uuid4()
        url_with_wrong_id = reverse('set-position', args=[wrong_id])

        payload = {
            'letter': 'A',
            'number': '1'
        }

        response = self.client.post(url_with_wrong_id, data=payload)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_set_piece_with_piece_different_from_knight_return_422(self):
        hook = ChessPiece.objects.create(type='hook', color='white')
        url_with_hook_id = reverse('set-position', args=[hook.id])

        payload = {
            'letter': 'A',
            'number': '1'
        }

        response = self.client.post(url_with_hook_id, data=payload)

        self.assertEqual(
            response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    def test_set_piece_successful_returns_list_with_possible_positions(self):
        payload = {
            'letter': 'A',
            'number': '1'
        }

        response = self.client.post(self.default_url, data=payload)
        expected_possible_positions = [
            ('A', '1'), ('A', '3'), ('A', '5'), ('B', '4'), ('C', '1'),
            ('C', '5'), ('D', '2'), ('D', '4'), ('E', '1'), ('E', '3')
        ]
        response_list = [
            (response_item['letter'], response_item['number'])
            for response_item in response.data
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            sorted(response_list), sorted(expected_possible_positions)
        )
