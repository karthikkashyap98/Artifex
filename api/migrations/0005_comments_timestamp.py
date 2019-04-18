# Generated by Django 2.2 on 2019-04-17 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
