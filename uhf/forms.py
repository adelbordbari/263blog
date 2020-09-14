from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

MAJOR_CHOICES = (
    ('barq', 'برق'),
    ('sanaye', 'صنایع'),
    ('olum', 'علوم کامپیوتر'),
    ('computer', 'کامپیوتر'),
    ('ryazi', 'ریاضیات'),
    ('shimi', 'شیمی'),
    ('omran', 'عمران'),
    ('-', 'سایر'),)


class Signup_Form(UserCreationForm):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}),
                           )
    stu_id = forms.IntegerField(label='Student ID',
                                max_value=99999999,
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control'}),
                                )
    major = forms.CharField(empty_value='-',
                            required=False,
                            widget=forms.Select(choices=MAJOR_CHOICES),
                            )
    email = forms.EmailField(widget=forms.EmailInput(
                                attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'name', 'stu_id',
                  'major', 'email', 'password1', 'password2']

    # to override the default inputs, which isnt centered and looks bad :)
    def __init__(self, *args, **kwargs):
        '''To bootstrap-ify default fields, like username'''
        super(Signup_Form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
