# Generated by Django 3.1.7 on 2021-05-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_cardetailtables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardetailtables',
            options={'verbose_name': 'Dodatkowa tabela strony auta', 'verbose_name_plural': 'Dodatkowe tabele strony auta'},
        ),
        migrations.AlterField(
            model_name='cardetailtables',
            name='title',
            field=models.CharField(editable=False, max_length=500, verbose_name='Kolumna'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='sub_title',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Tytuł mały'),
        ),
    ]