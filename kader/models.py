from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING

GRADES = [("6K", "6. Kyu"), ("5K", "5. Kyu"), ("4K", "4. Kyu"), ("3K", "3. Kyu"), ("2K", "2. Kyu"), ("1K", "1. Kyu"),
          ("1D", "1. Dan"), ("2D", "2. Dan"), ("3D", "3. Dan"), ("4D", "4. Dan"), ("5D", "5. Dan"), ("6D", "6. Dan"),
          ("7D", "7. Dan"), ("8D", "8. Dan")]

POINTS = [("M", "M"), ("K", "K"), ("D", "D"), ("T", "T"), ("I", "I")]


class Member(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()

    gender = models.CharField(max_length=1, choices=(("m", "male"), ("f", "female")))
    active = models.BooleanField()

    grade = models.CharField(max_length=10, null=True, blank=True, choices=GRADES)
    zekken = models.BooleanField()
    jacket = models.BooleanField()

    def __str__(self):
        return self.name + ", " + self.first_name


class Training(models.Model):
    date = models.DateField()
    attended = models.ManyToManyField(Member)

    def __str__(self):
        return str(self.date)


class Fight(models.Model):
    red = models.ForeignKey(Member, on_delete=DO_NOTHING, related_name='+')
    white = models.ForeignKey(Member, on_delete=DO_NOTHING, related_name='+')
    red_point_one = models.CharField(max_length=1, null=True, blank=True, choices=POINTS)
    red_point_two = models.CharField(max_length=1, null=True, blank=True, choices=POINTS)
    white_point_one = models.CharField(max_length=1, null=True, blank=True, choices=POINTS)
    white_point_two = models.CharField(max_length=1, null=True, blank=True, choices=POINTS)
    training = models.ForeignKey(Training, on_delete=DO_NOTHING, null=True, related_name="fights")
