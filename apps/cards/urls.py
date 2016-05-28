from django.conf.urls import url
from .views import view_card

urlpatterns = [
    url(r'^(?P<card_id>\d+)/$', view_card),
]
