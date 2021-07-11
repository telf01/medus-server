from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('get-patient/<str:pk>/', views.getPatient, name="get-patient"),
    path('get-token', views.getToken, name="get-token"),
]
