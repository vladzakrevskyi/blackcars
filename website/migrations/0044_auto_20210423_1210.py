# Generated by Django 3.1.7 on 2021-04-23 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_servicepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicepage',
            options={'verbose_name': 'Tabele strony usług', 'verbose_name_plural': 'Tabele strony usług'},
        ),
        migrations.CreateModel(
            name='ServiceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(help_text='Wprowadź nazwę usługi', max_length=800, verbose_name='Nazwa usługi')),
                ('service_price', models.CharField(help_text='Wprowadź cenę usługi', max_length=800, verbose_name='Cena usługi')),
                ('servicepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='website.servicepage')),
            ],
            options={
                'verbose_name': 'Tabele strony usług',
                'verbose_name_plural': 'Tabele strony usług',
            },
        ),
    ]
