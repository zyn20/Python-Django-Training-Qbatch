from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

handler404 = "students.views.custom_404_view"

urlpatterns = [
    path("create/", views.create_student, name="create_student"),
    path("success/", views.success, name="success"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("myasyncview/", views.my_async_view, name="async"),
]
