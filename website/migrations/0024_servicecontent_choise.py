# Generated by Django 3.1.7 on 2021-03-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20210316_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecontent',
            name='choise',
            field=models.CharField(choices=[('Zdjęcie po lewej', 'Zdjęcie po lewej'), ('Zdjęcie po prawej', 'Zdjęcie po prawej')], default='Zdjęcie po lewej', max_length=100),
        ),
    ]
