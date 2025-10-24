from django import forms  # Импортируем формы Django
from .models import Article


class ArticleForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label='Название статьи')
    body = forms.CharField(max_length=200, required=True, label='Содержание')
    
    class Meta:
        model = Article
        fields = ['name', 'body']
        # labels = {
        #     'name': 'Название статьи',      # ваше кастомное имя для поля 'name'
        #     'body': 'Содержание',           # для 'body'
        # }
