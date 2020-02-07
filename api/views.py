from rest_framework.generics import ListCreateAPIView

from api.models import ChessPiece
from api.serializers import ChessPieceSerializer


class RegisterPieceView(ListCreateAPIView):
    queryset = ChessPiece.objects.all()
    serializer_class = ChessPieceSerializer
