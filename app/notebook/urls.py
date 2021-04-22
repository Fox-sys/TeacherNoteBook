from django.urls import path
from .views import IndexDetailView

urlpatterns = [
    path('', IndexDetailView.as_view(), name="index"),
]
