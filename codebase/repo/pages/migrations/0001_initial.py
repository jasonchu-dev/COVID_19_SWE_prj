# Generated by Django 3.2.8 on 2021-10-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_E', models.CharField(max_length=220)),
                ('percent', models.IntegerField()),
            ],
        ),
    ]
