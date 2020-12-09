from django import forms
from main.models import Article
from main.models import Contact


class BootstapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})

class SearchForm(BootstapForm):
    search = forms.CharField(label='поиск', max_length=1000, empty_value='поиск')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    #subject = forms.CharField(label='Тема', max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    #email = forms.EmailField(label='e-mail', widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    #message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'style': 'height: 10em', 'class': 'form-control'}))