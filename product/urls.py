from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.detail, name='detail'),
]