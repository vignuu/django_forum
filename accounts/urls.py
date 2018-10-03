from django.urls import path
from accounts import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name = 'signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]