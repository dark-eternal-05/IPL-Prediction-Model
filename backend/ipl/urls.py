from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeamViewSet, PlayerViewSet, MatchViewSet,
    PlayerPerformanceViewSet, PredictionViewSet, PredictAPIView
)
from .consumers import MatchUpdateConsumer

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'performances', PlayerPerformanceViewSet)
router.register(r'predictions', PredictionViewSet)

websocket_urlpatterns = [
    path('ws/live/', MatchUpdateConsumer.as_asgi()),
]

urlpatterns = [
    path('', include(router.urls)),
    path('predict/', PredictAPIView.as_view(), name='predict'),
]
