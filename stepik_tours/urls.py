from django.contrib import admin
from django.urls import include, path, re_path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    re_path(r'^departure/', include('tours.urls')),
    re_path(r'^tour/', include('tours.urls')),

]
