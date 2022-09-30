from django.urls import path
from . import views

urlpatterns = [
    path('logbook/', views.DiveList.as_view(), name='logbook'),
    path('logbook/<slug:slug>', views.DiveDetails.as_view(), name='dive_details'),
]
