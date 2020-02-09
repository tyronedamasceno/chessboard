from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.enum import ChessPieceType
from api.models import ChessPiece
from api.serializers import ChessPieceSerializer, AlgebricNotationSerializer
from api.utils import find_knight_possible_moves_in_two_turns


class RegisterPieceViewSet(ListCreateAPIView):
    queryset = ChessPiece.objects.all()
    serializer_class = ChessPieceSerializer


class SetPiecePositionView(APIView):
    @swagger_auto_schema(request_body=AlgebricNotationSerializer,
                         responses={'200': AlgebricNotationSerializer})
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

        return Response(data=sorted(list(possible_moves)))
