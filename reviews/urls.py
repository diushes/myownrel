from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    path('reviews/', Reviewview.as_view(), name='reviews'),


]