from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('get-patient/<str:pk>/', views.getPatient, name="get-patient"),
    path('get-token', views.getToken, name="get-token"),
    path('add-note', views.addNote, name="add-note"),
    path('get-notes/<str:pk>/', views.getNotes, name="get-notes"),
]
