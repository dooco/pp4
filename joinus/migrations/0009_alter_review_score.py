# Generated by Django 4.1.5 on 2023-02-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0008_remove_review_email_remove_review_name_review_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
