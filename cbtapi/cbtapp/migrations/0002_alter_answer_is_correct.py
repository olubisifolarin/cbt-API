# Generated by Django 3.2 on 2022-05-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]