from django.urls import path, include

from Web_Store.accounts import views

urlpatterns = (
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.get_profile_details, name='profile-details'),
        path('delete/', views.delete_profile, name='delete-profile'),
        path('edit/', views.UserEditView.as_view(), name='edit-profile'),

    ]))
)
