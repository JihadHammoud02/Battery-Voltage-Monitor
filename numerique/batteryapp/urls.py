from django.urls import path
import views
from batteryapp.views import show_perc,getThreshold
app_name = 'batteryapp'
urlpatterns = [
    path('',show_perc,name='show_perc'),
    path('hello/',getThreshold,name='getThreshold'),
    path('index/',views.index,name='index')
]