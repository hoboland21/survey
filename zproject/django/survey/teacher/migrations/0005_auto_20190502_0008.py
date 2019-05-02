# Generated by Django 2.2 on 2019-05-02 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190501_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
