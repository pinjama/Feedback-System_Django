from django.urls import path, include
from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedbackCreateView.as_view(), name='index'),
]