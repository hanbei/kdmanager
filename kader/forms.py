from django import forms

from kdmgmt2.kader import models
from kdmgmt2.kader.models import Member, Fight


class MemberForm(forms.Form):
    name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    email = forms.EmailField()

    gender = forms.CharField(max_length=1, choices=(("m", "male"), ("f", "female")))
    active = forms.BooleanField()

    grade = forms.CharField(max_length=10, null=True, blank=True, choices=models.GRADES)
    zekken = forms.BooleanField()
    jacket = forms.BooleanField()


class TrainingForm(forms.Form):
    date = forms.DateField()
    members = forms.ModelMultipleChoiceField(Member.objects.all())


class FightForm(forms.Form):
    red = forms.ModelMultipleChoiceField(Fight.objects.all())
    white = forms.ModelMultipleChoiceField(Fight.objects.all())
    red_point_one = forms.CharField(max_length=1, null=True, blank=True, choices=models.POINTS)
    red_point_two = forms.CharField(max_length=1, null=True, blank=True, choices=models.POINTS)
    white_point_one = forms.CharField(max_length=1, null=True, blank=True, choices=models.POINTS)
    white_point_two = forms.CharField(max_length=1, null=True, blank=True, choices=models.POINTS)
