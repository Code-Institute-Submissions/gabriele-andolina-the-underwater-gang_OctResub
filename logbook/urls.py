from . import views
from django.urls import path

urlpatterns = [
    path('logbook/', views.DiveList.as_view(), name='logbook'),
]
