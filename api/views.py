from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.enum import ChessPieceType
from api.models import ChessPiece
from api.serializers import ChessPieceSerializer, AlgebricNotationSerializer
from api.utils import find_knight_possible_moves_in_two_turns


class RegisterPieceViewSet(CreateAPIView):
    queryset = ChessPiece.objects.all()
    serializer_class = ChessPieceSerializer


class SetPiecePositionView(APIView):
    def post(self, request, piece_id):
        serializer = AlgebricNotationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        piece = get_object_or_404(ChessPiece, id=piece_id)

        if piece.type != ChessPieceType.knight.value:
            return Response(
                data={'message': f'The requested piece is {piece}'},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        possible_moves = find_knight_possible_moves_in_two_turns(
            **validated_data
        )

        possible_moves_dict = [
            {'letter': letter, 'number': number}
            for letter, number in possible_moves
        ]

        serializer = AlgebricNotationSerializer(possible_moves_dict, many=True)

        return Response(data=serializer.data)
