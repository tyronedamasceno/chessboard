from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from api.models import ChessPiece
from api.serializers import ChessPieceSerializer


class RegisterPieceViewSet(CreateModelMixin, GenericViewSet):
    queryset = ChessPiece.objects.all()
    serializer_class = ChessPieceSerializer
