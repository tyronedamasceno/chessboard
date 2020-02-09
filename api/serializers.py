from rest_framework import serializers

from api.models import ChessPiece


class ChessPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessPiece
        fields = ('id', 'type', 'color')
        read_only_fields = ('id', )


class AlgebricNotationSerializer(serializers.Serializer):
    letter = serializers.CharField(max_length=1)
    number = serializers.CharField(max_length=1)
