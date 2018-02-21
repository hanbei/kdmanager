import csv

from django.core.management import BaseCommand

from kader.models import Member


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str)

    def handle(self, *args, **options):
        f = options['file'][0]
        with open(f, 'r') as csv_file:
            reader = csv.reader(csv_file )
            next(reader)
            for row in reader:
                print(row)
                recipe = Member(name=row[0], first_name=row[1], birth_date=row[2], gender=row[3], grade=row[4],
                                email=row[5], zekken=row[7], jacket=row[8], active=True)
                recipe.save()
