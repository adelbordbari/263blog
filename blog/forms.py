from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # to create form fields
    '''
    we can't stylize form components when we don't use the class below
    but doing this helps to pass attributes to each tag in the html files.
    '''
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'tags', 'body')
        widgets = {  # add the component attrs, all are text inputs except author
            # pass any atr:val as div items based on bootstrap classes
            # also tweak the form in html and wrap it in a <div class="form-group">
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title'}),

            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A short name'}),

            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'type': 'hidden',
                #to identify with css
                'id': 'author_input'}),
                
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Start writing...', }),
        }


class EditForm(forms.ModelForm):  # to create form fields
    class Meta:
        model = Post
        fields = ['title', 'tags', 'body']
        widgets = {  # add the component attrs, all are text inputs except author
            # pass any atr:val as div items based on bootstrap classes
            # also tweak the form in html and wrap it in a <div class="form-group">
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a title for your post...',
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write about anything...',
            }),
        }
