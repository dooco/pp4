# Generated by Django 4.1.5 on 2023-02-11 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
