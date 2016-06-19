""""Filter."""
from django import template
# from requests import request
from apps.cards.models import Cards
register = template.Library()


@register.filter
def private(cards, request):
    if request.user.is_authenticated():
        private_cards = Cards.objects.filter(user=request.user, private=True)
    else:
        private_cards = None
    return private_cards


@register.filter
def public(cards):
    public_cards = Cards.objects.filter(private=False)
    return public_cards
