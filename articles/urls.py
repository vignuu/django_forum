from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from djangoforum import views
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$',views.index,name='index'),
]
