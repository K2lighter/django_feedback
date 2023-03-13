from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', min_length=2, max_length=7, error_messages={
#         'min_length': 'Слишком мало символов',
#         'max_length': 'Слишком много символов',
#         'required': 'Укажите хотя бы один символ',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)
#

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'rating', ]
        # exclude = ['rating']
        fields = '__all__'
        labels = {
            'name': "Имя",
            'surname': "Фамилия",
            'rating': "Рейтинг",
            'feedback': "Отзыв"
        }
        error_message = {
            'name': {
                'max_length': 'error max',
                'min_length': 'error min',
                'required': "error required"
            }
        }
