# Generated by Django 3.1.7 on 2021-03-12 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210312_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='slug_posts',
        ),
    ]
