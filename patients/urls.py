from django.urls import path
from . import views

urlpatterns = [
    path('', views.plist),
    path('add/', views.add),
    path('add-user/', views.addUser),
    path('qr-test/<str:uuid>/', views.qrTest)
]
