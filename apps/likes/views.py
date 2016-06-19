from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# from .models import Cards, Likes
from .models import Likes
from apps.cards.models import Cards

from apps.cards.views import view_card
# Create your views here.


@login_required(login_url='/users/login/')
def like(request, card_id):
    card = Cards.objects.get(id=card_id)

    like1 = Likes.objects.get_or_create(card=card)
    like1 = like1[0]
    for x in like1.user.all():
        if x == request.user:
            like1.user.remove(request.user)
            return redirect(view_card, card_id=card_id)

    like = Likes.objects.get(card=card)
    like.user.add(request.user)
    return redirect(view_card, card_id=card_id)
