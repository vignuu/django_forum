from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]