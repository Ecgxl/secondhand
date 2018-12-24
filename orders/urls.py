from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/<int:product_id>/', views.order_create, name='order_create'),
    # path('sucessfully/<int:product_id>/',views.receive,name='order_create')
]
