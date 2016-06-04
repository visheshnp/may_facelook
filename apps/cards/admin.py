from django.contrib import admin
from .models import Cards

# Register your models here.


class UserProfileInfoAdmin(admin.ModelAdmin):
    """Customising admin view of UserProfileInfo class."""

    readonly_fields = ['card_created']

    class Meta:
        """Information of this class."""

        model = Cards

admin.site.register(Cards, UserProfileInfoAdmin)
