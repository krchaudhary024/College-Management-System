# Generated by Django 4.1 on 2022-08-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
