from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('check',views.show,name='show'),
    path('get-weather/', views.get_weather, name='get_weather'),
]