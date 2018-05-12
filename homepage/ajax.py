from django.http import HttpResponse
import json
from joboffers.models import Offer, City


def get_position(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        positions = Offer.objects.filter(position__icontains=q)
        results = []
        for pl in positions:
            place_json = {}
            place_json = pl.position
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_city(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        positions = City.objects.filter(city__icontains=q)
        results = []
        for pl in positions:
            place_json = {}
            place_json = pl.city
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)