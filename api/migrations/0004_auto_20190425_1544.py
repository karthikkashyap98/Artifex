# Generated by Django 2.2 on 2019-04-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
