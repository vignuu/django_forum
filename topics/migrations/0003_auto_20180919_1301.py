# Generated by Django 2.1.1 on 2018-09-19 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20180918_1005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='answervotes',
            options={'verbose_name_plural': 'Answer Votes'},
        ),
        migrations.AlterModelOptions(
            name='topiccontributors',
            options={'verbose_name_plural': 'Topic Contributors'},
        ),
        migrations.AlterModelOptions(
            name='topics',
            options={'verbose_name_plural': 'Topics'},
        ),
    ]
