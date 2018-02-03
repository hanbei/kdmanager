from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()

    gender = models.CharField(max_length=1, choices=(("m", "male"), ("f", "female")))
    active = models.BooleanField()

    grade = models.CharField(max_length=10, null=True, blank=True, choices=[
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
    zekken = models.BooleanField()
    jacket = models.BooleanField()

class Attendance(models.Model):
    date = models.DateField()
    attended = models.ManyToManyField(Member)