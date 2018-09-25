from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from articles import views
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    url(r'^index/$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^sample/$',views.sample,name='sample'),
    url(r'^scroll/$',views.scroll,name='scroll'),
]


