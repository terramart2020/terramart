from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.view_product, name='view_product'),
    path('create/', views.create_product, name='create_product'),
]