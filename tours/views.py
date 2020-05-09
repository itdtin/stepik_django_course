from django.views import View
from django.http import Http404
from django.shortcuts import render

from .tours_data import tours, departures, title, description, subtitle


class MainView(View):
    """Класс представления для главной"""

    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={
                'title': title, 'subtitle': subtitle,
                'description': description, 'tours': [tours[tour] for tour in tours],
                'departures': departures}
        )


class DepartureView(View):
    """Класс представления для направлений"""

    def get(self, request, departure_name, *args, **kwargs):

        if departure_name not in departures:
            raise Http404

        return render(
            request, 'tours/departure.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departure': departures[departure_name],
                'departures': departures,
                'tours': [tours[tour] for tour in tours if tours[tour]['departure'] == departure_name]}
        )


class TourView(View):
    """Класс представления для каждого тура"""

    def get(self, request, id, *args, **kwargs):
        id = int(id)
        if id not in tours:
            raise Http404

        return render(request, 'tours/tour.html')
