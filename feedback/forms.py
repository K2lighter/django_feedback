from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=2, max_length=7, error_messages={
        'min_length': 'Слишком мало символов',
        'max_length': 'Слишком много символов',
        'required': 'Укажите хотя бы один символ',
    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


