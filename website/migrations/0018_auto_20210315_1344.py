# Generated by Django 3.1.7 on 2021-03-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20210313_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='options',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='website.car'),
        ),
    ]
