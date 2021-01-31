from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('<int:category_id>/', views.view_category, name='view_category'),
    path('create/', views.create_category, name='create_category'),
]