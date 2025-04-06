from django.urls import path
from .views import RegistrationView,LoginView,LogoutView,CustomTokenRefreshView,EditProfileView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("update-profile/", EditProfileView.as_view(), name="update_profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh")
]
