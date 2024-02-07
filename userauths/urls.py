from django.urls import path

from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', views.register_user, name='sign-up'),
    path('sign-in/', views.login_user, name='sign-in'),
    path('sign-out/', views.logout_user, name='sign-out'),
]
