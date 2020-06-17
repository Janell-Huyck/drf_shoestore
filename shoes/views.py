from django.shortcuts import render

from shoes.models import Shoe


def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {'shoes': shoes})
