from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comments"]
        # fields = ["comments", "cards", "user"]
