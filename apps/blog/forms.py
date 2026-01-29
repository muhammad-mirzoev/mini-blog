from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'status',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 8,
                    'placeholder': 'Напишите текст поста...',
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 5:
            raise ValidationError('Заголовок должен быть не менее 5 символов')

        return title

    def clean_content(self):
        content = self.cleaned_data['content'].strip()

        if len(content) > 50:
            raise ValidationError(
                'Контент должен быть не менее 50 символов'
            )

        return content
