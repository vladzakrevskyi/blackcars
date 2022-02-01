# Generated by Django 3.1.7 on 2021-03-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_auto_20210325_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option_Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Nazwa opcji')),
                ('option_desc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Opis opcji')),
                ('option_price', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cena opcji')),
                ('choise', models.CharField(choices=[('Zawarte w cenie', 'Zawarte w cenie'), ('', '')], default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Opcja',
                'verbose_name_plural': 'Opcje',
            },
        ),
        migrations.RemoveField(
            model_name='mainslider',
            name='slug_1',
        ),
        migrations.RemoveField(
            model_name='mainslider',
            name='slug_2',
        ),
    ]