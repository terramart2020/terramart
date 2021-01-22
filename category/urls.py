from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('<int:category_id>/', views.detail, name='detail'),
]