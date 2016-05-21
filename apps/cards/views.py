from django.shortcuts import render
from .models import Cards
# Create your views here.


def home(request):
    """Display all cards."""
    context = {}
    cards = Cards.objects.all()
    context = {'cards': cards}
    template = 'home.html'
    return render(request, template, context)
