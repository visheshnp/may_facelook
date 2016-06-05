"""URL configuration for Comments."""
from django.conf.urls import url
from apps.comments.views import comment

urlpatterns = [
    url(r'^comment/(?P<card_id>\d+)/$', comment, name="comment"),
]
