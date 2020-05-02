from django.urls import path
from .views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('departure/<str:departure_name>', DepartureView.as_view(), name='departure'),
    path('tour/<int:id>/', TourView.as_view(), name='tour'),
]
