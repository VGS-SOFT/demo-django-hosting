from django.urls import path
from .views import HealthCheckView, WebSocketTestView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('ws-test/', WebSocketTestView.as_view(), name='ws-test'),
]
