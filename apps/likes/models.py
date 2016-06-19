from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Likes(models.Model):
    user = models.ManyToManyField(
        User,
        default='')

    card = models.OneToOneField(
        'cards.Cards',
        default='')

    time = models.DateTimeField(
        default=timezone.now)

    def get_likes_count(self):
        return self.user.count()

    def __unicode__(self):
        return str(self.card)
