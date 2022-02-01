# Generated by Django 3.1.7 on 2021-03-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20210324_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSLider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1500, verbose_name='Tytuł duży')),
                ('sub_title', models.CharField(blank=True, max_length=1500, verbose_name='Tytuł mały')),
                ('images', models.ImageField(blank=True, upload_to='main_slider', verbose_name='Zdjęcie')),
            ],
            options={
                'verbose_name': 'SLider(Strona główna)',
                'verbose_name_plural': 'SLider(Strona główna)',
            },
        ),
    ]
