from django.urls import path
from . import views

urlpatterns = [
    path('logbook/', views.DiveList.as_view(), name='logbook'),
]
