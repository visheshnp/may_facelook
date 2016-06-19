from django.conf.urls import url
from .views import like

urlpatterns = [
    url(r'^(?P<card_id>\d+)/$', like, name='like'),
]
