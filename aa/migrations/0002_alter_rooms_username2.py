# Generated by Django 5.0.4 on 2024-07-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='username2',
            field=models.CharField(max_length=11, null=True),
        ),
    ]