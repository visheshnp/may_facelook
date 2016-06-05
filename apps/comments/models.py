"""Model class for comments app."""
from django.db import models
from django.contrib.auth.models import User
# from apps.cards.models import Cards
# Create your models here.


class Comments(models.Model):
    """Comments for cards."""

    user = models.ForeignKey(
        User,
        default="",
        null=False,
        blank=False)

    cards = models.ForeignKey(
        'cards.Cards',
        default="",
        null=False,
        blank=False)

    comments = models.TextField(
        null=False,
        blank=False,
        default="",
        verbose_name='Comments',
        help_text='You can give your thoughts for the card.')

    def __unicode__(self):
        """Unicode for Comments."""
        return str(self.cards.card_title)
