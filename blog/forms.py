from django import forms
from blog.models import *

CATEGORY = Category.objects.all()

class SearchForm(forms.Form):
    s = forms.CharField(max_length=20)

class ArticleForm(forms.Form):
    title = forms.CharField(required=True, max_length=50)
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ModelChoiceField(queryset=CATEGORY, empty_label='请选择分类')

