from django.urls import path
from . import views
from .views import feedback_view,feedback_success_view

urlpatterns = [
    path('', views.index, name = 'index'),
    path('vote/<str:pk>', views.vote, name = 'vote'),
    path('result/<str:pk>', views.result, name = 'result'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success_view, name='feedback_success')
]