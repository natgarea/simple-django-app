# Generated by Django 3.1 on 2020-08-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tax_number',
            field=models.IntegerField(default=9, verbose_name='Tax number'),
            preserve_default=False,
        ),
    ]
