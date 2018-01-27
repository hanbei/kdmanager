# Generated by Django 2.0.1 on 2018-01-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('active', models.BooleanField()),
                ('grade', models.CharField(blank=True, choices=[('6K', '6. Kyu'), ('5K', '5. Kyu'), ('4K', '4. Kyu'), ('3K', '3. Kyu'), ('2K', '2. Kyu'), ('1K', '1. Kyu'), ('1D', '1. Dan'), ('2D', '2. Dan'), ('3D', '3. Dan'), ('4D', '4. Dan'), ('5D', '5. Dan'), ('6D', '6. Dan'), ('7D', '7. Dan'), ('8D', '8. Dan')], max_length=10, null=True)),
                ('zekken', models.BooleanField()),
                ('jacket', models.BooleanField()),
            ],
        ),
    ]