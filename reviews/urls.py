from django.urls import path
from . import views
urlpatterns = [
    path('', views.review, name='index'),
    path('thank-you/', views.thank_you)
]