# Generated by Django 3.2 on 2021-04-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210420_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membermodel',
            options={'verbose_name_plural': 'MEMBERS'},
        ),
        migrations.AlterModelOptions(
            name='skillmodel',
            options={'verbose_name_plural': 'SKILLS'},
        ),
        migrations.RenameField(
            model_name='skillmodel',
            old_name='skil_name',
            new_name='skill_name',
        ),
    ]