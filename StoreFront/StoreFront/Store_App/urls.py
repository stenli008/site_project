from django.urls import path
from .views import *

urlpatterns = (
    path('1/', store, name='store'),
)

