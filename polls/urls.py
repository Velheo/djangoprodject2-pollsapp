from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('results/<int:pk>', views.results, name="results"),
    path('vote/<int:pk>', views.vote, name="vote"),
]