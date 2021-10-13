from django.db import models
import os

# Create your models here.
info = []
with open (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'demographics.csv'), 'r') as csvfile:
    with open ("demographics.json", 'w') as jsonfile:
        for row in csvfile:
            info = row.split(',')
            jsonfile.write(' '.join(info))
