from django import forms

from kader import models
from kader.models import Member, Fight


class MemberForm(forms.Form):
    name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    email = forms.EmailField()

    gender = forms.ChoiceField(choices=(("m", "male"), ("f", "female")))
    active = forms.BooleanField()

    grade = forms.ChoiceField(choices=models.GRADES)
    zekken = forms.BooleanField()
    jacket = forms.BooleanField()


class TrainingForm(forms.Form):
    date = forms.DateField()
    members = forms.ModelMultipleChoiceField(queryset=Member.objects.all())#, choices=Member.objects.all())


class FightForm(forms.Form):
    red = forms.ModelMultipleChoiceField(Fight.objects.all())
    white = forms.ModelMultipleChoiceField(Fight.objects.all())
    red_point_one = forms.ChoiceField(choices=models.POINTS)
    red_point_two = forms.ChoiceField(choices=models.POINTS)
    white_point_one = forms.ChoiceField(choices=models.POINTS)
    white_point_two = forms.ChoiceField(choices=models.POINTS)


class EmailForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    email_text = forms.CharField(label='Email', widget=forms.Textarea)
