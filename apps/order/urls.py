from django.urls import path
from .views import OrderListCreateAPIView

urlpatterns = [
    path('order/', OrderListCreateAPIView.as_view(), name='order-create')
]