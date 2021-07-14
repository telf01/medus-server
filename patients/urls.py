from django.urls import path
from . import views

urlpatterns = [
    path('', views.plist, name='home'),
    path('add/', views.add, name='add'),
    path('add-user/', views.addUser),
    path('qr-test/<str:uuid>/', views.qrTest),
    path('login/', views.login)
]
