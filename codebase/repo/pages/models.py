from django.db import models

# Create your models here.
info = []
with open ("demographics.csv", 'r') as csvfile:
    with open ("demographics.json", 'w') as jsonfile:
        for row in csvfile:
            info = row.split(',')
            jsonfile.write(' '.join(info))
