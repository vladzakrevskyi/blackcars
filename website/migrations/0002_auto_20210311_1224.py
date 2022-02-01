# Generated by Django 3.1.7 on 2021-03-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='service',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Sortowanie'),
        ),
        migrations.AddField(
            model_name='service',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Zdjęcie w tytułe', null=True, upload_to='service_background_image', verbose_name='Zdjęcie w tytułe'),
        ),
    ]