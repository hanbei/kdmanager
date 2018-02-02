from django import forms

class MemberForm(forms.Form):
    name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    email = forms.EmailField()

    gender = forms.CharField(max_length=1, choices=(("m", "male"), ("f", "female")))
    active = forms.BooleanField()

    grade = forms.CharField(max_length=10, null=True, blank=True, choices=[
        ("6K", "6. Kyu"),
        ("5K", "5. Kyu"),
        ("4K", "4. Kyu"),
        ("3K", "3. Kyu"),
        ("2K", "2. Kyu"),
        ("1K", "1. Kyu"),
        ("1D", "1. Dan"),
        ("2D", "2. Dan"),
        ("3D", "3. Dan"),
        ("4D", "4. Dan"),
        ("5D", "5. Dan"),
        ("6D", "6. Dan"),
        ("7D", "7. Dan"),
        ("8D", "8. Dan")
    ])
    zekken = forms.BooleanField()
    jacket = forms.BooleanField()