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


def view_card(request, card_id):
    """Display specific card."""
    context = {}
    card = Cards.objects.get(id=card_id)
    context = {'card': card}
    template = 'view_card.html'
    return render(request, template, context)
