from django.urls import path

from orders.views import MyOrderView


urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name='my_order'),
]
