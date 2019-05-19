# Generated by Django 2.2.1 on 2019-05-16 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacher.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='grade_level',
            field=models.CharField(default='00', max_length=4),
            preserve_default=False,
        ),
    ]
