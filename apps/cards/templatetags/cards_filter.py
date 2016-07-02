""""Filter."""
from django import template
# from requests import request
# from apps.cards.models import Cards
register = template.Library()


@register.filter
def like_users(likes):
    user_list = []
    for user in likes.user.all():
        user_list.append(user.username)

    return user_list


@register.filter
def private(cards, request):
    cards_list = []
    if request.user.is_authenticated():
        for card in cards:
            if card.private is True and card.user == request.user:
                cards_list.append(card)

    return cards_list


@register.filter
def public(cards):
    cards_list = []
    for card in cards:
        if card.private is False:
            cards_list.append(card)

    return cards_list


@register.filter
def all_cards(cards, request):
    cards_list = []
    for card in cards:
        if card.private is False:
            cards_list.append(card)

    if request.user.is_authenticated():
        for card in cards:
            if card.private is True and card.user == request.user:
                cards_list.append(card)

    return cards_list
