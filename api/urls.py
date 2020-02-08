from django.urls import path, include

from rest_framework import routers

from api.views import RegisterPieceViewSet

router = routers.DefaultRouter()
router.register('pieces', RegisterPieceViewSet, basename='pieces')


urlpatterns = [
    path('', include(router.urls))
]
