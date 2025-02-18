from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)])
        }
        labels = {
            'text': 'Ваш отзыв',
            'rating': 'Оценка',
        }