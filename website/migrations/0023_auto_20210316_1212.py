# Generated by Django 3.1.7 on 2021-03-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20210316_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecontent',
            name='title',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Tytuł bloku'),
        ),
    ]