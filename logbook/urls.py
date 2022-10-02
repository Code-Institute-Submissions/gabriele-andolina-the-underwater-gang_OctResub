from django.urls import path
from . import views

urlpatterns = [
    path('logbook/', views.DiveList.as_view(), name='logbook'),
    path('logbook/<slug:slug>', views.DiveDetails.as_view(), name='dive_details'),
    path('logbook/log-a-dive/', views.LogDive.as_view(), name='log_dive'),
    path('logbook/update/<slug:slug>', views.UpdateDive.as_view(), name='update_dive'),
]
