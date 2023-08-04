from django.urls import path

from Web_Store.Store_App import views

urlpatterns = (
    path('', views.store, name='store'),
)