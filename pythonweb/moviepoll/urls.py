from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/result/', views.result, name='result'),
]
