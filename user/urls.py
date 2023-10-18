from django.urls import path
from .views import UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_user/', UserEditView.as_view(), name='edit-user'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="profile-user"),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name="edit-profile-user"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile"),
]
