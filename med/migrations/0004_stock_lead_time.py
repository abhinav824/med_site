# Generated by Django 2.1.7 on 2019-04-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0003_auto_20190405_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='lead_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
