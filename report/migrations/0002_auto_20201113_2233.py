# Generated by Django 3.1.2 on 2020-11-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]