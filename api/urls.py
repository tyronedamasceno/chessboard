from django.urls import path, include

from rest_framework import routers

from api.views import RegisterPieceView

router = routers.DefaultRouter()
router.register('pieces', RegisterPieceView, basename='pieces')


urlpatterns = [
    path('', include(router.urls))
]
