# Generated by Django 3.2 on 2021-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membermodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=10),
        ),
    ]
