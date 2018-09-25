from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from articles import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'

urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
