from django.urls import path


from Web_Store.Store_App import views

urlpatterns = (
    path('', views.store_view, name='store'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
)


