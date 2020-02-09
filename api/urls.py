from django.urls import path

from api.views import RegisterPieceViewSet, SetPiecePositionView


urlpatterns = [
    path('pieces', RegisterPieceViewSet.as_view(), name='pieces'),
    path(
        'pieces/<uuid:piece_id>/position', SetPiecePositionView.as_view(),
        name='set-position'
    )
]
