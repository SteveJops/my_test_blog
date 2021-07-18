from django import forms
from .models import News


class NewsForm(forms.Form):
    class Meta:
        model = News
        fields = ['user', 'slug', 'title', 'text_min', 'text', 'image']

        forms.widgets = {
            'user': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class':"form-control"}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text_min': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ImageField(),
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug =='create':
                raise forms.ValidationError("Slug may not be 'Create'")
            return new_slug
