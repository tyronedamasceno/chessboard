from rest_framework import serializers

from api.models import ChessPiece


class ChessPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessPiece
        fields = ('id', 'type', 'color')
        read_only_fields = ('id', )
