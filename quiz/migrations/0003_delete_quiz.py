# Generated by Django 4.0.4 on 2022-05-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quiz_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
