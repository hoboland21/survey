# Generated by Django 2.2 on 2019-05-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20190501_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='group',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='label',
        ),
        migrations.AddField(
            model_name='survey',
            name='locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='url',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
