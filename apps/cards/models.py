from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Cards(models.Model):
    user = models.ForeignKey(
        User,
        default='',
        blank=True,
        null=True,
        verbose_name="related user")

    card_title = models.CharField(
        max_length=255,
        blank=False,
        null=False)

    card_description = models.TextField(
        blank=False,
        null=False,
        verbose_name='card_description')

    card_hero_image = models.ImageField(
        upload_to='Cards',
        blank=False,
        null=False,
        default='',
        verbose_name='Card display image',
        help_text='Add')

    private = models.BooleanField(
        default=False)

    card_created = models.DateTimeField(
        default=timezone.now)

    def __unicode__(self):
        """Unicode Method to Display Relevent data in Admin."""
        return self.card_title

    class Meta:
        """Information About the class."""

        verbose_name = "Card"
        verbose_name_plural = "Cards"
