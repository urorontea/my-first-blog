# Generated by Django 3.2.5 on 2022-08-23 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_rename_title_post_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title1',
            new_name='title',
        ),
    ]
