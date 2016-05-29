from django.conf.urls import url
from .views import view_card, create_card

urlpatterns = [
    url(r'^(?P<card_id>\d+)/$', view_card),
    url(r'^create_card/$', create_card, name='create_card'),
]
