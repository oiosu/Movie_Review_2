from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
]
