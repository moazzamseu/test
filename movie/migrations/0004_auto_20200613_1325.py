# Generated by Django 3.0.7 on 2020-06-13 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movielink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movielink',
            old_name='links',
            new_name='link',
        ),
    ]