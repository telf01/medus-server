from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('patient-get/<str:pk>/', views.getPatient, name="patient-get"),
]
