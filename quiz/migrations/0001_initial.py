# Generated by Django 4.0.4 on 2022-05-21 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('optionOne', models.CharField(max_length=255)),
                ('optionTwo', models.CharField(max_length=255)),
                ('optionThree', models.CharField(max_length=255)),
                ('optionFour', models.CharField(max_length=255)),
                ('optionFive', models.CharField(max_length=255)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
