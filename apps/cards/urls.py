from django.conf.urls import url
from .views import view_card, create_card, private_cards, search

urlpatterns = [
    url(r'^(?P<card_id>\d+)/$', view_card, name='view_card'),
    url(r'^private/$', private_cards, name='private_cards'),
    url(r'^create_card/$', create_card, name='create_card'),
    url(r'^search/$', search, name='search'),
]
