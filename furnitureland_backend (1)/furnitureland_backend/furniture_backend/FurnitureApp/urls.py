from django.urls import re_path
from FurnitureApp import views

urlpatterns = [
    re_path(r'^item$', views.furnitureApi),
    re_path(r'^item/([0-9]+)$', views.furnitureApi),

    re_path(r'^user/reg$', views.userRegApi),

    re_path(r'^user/login$', views.userLoginApi),

    re_path(r'^all-users$', views.getAllUsersApi),
]
