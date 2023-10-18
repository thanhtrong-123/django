from django import forms
from .models import Post, Comment, Category

#choices = [('coding', 'coding'), ('sports', 'sports'),]
choices = Category.objects.all().values_list('name','name')

choices_list = []

for item in choices:
    choices_list.append(item)

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','category', 'body','header_image' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'id_current', 'type':'hidden'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' ,'type':'hidden', 'value':'','id':'tai'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),     
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','body','draft')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            
            
        }