# Generated by Django 4.1.5 on 2023-02-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardfeature',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature', to='joinus.category'),
        ),
    ]
