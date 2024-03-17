from django.urls import path ,include
from . import  views

urlpatterns = [
    path('register/',views.RegisterApiView.as_view(),name="register"),
    path('login/',views.LoginApiView.as_view(),name="login")
]
