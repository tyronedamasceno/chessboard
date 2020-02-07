from django.db import models

from api.enum import ChessPieceColor, ChessPieceType


class ChessPiece(models.Model):
    type = models.CharField(max_length=20, choices=ChessPieceType.choices())
    color = models.CharField(max_length=20, choices=ChessPieceColor.choices())
