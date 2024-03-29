# Generated by Django 3.2 on 2021-06-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255, verbose_name='Nazwa pojazdu')),
                ('nr_rej', models.CharField(max_length=10, verbose_name='Numer rejestracyjny')),
                ('typ_pojazdu', models.CharField(choices=[('O', 'Samochód osobowy'), ('M', 'Motocykl')], default='O', max_length=2, verbose_name='Typ pojazdu')),
                ('uwagi', models.TextField(verbose_name='Uwagi')),
                ('rok_produkcji', models.PositiveIntegerField(default='1965', verbose_name='Rok produkcji')),
                ('przebieg', models.PositiveIntegerField(default='1', verbose_name='Przebieg')),
                ('przeglad_techniczny', models.DateField(default='1965-01-01', verbose_name='Przegląd techniczny do')),
                ('ubezpieczenie', models.DateField(default='1965-01-01', verbose_name='Ubezpieczenie do')),
                ('wymiana_oleju', models.DateField(default='1965-01-01', verbose_name='Wymiana oleju do')),
            ],
            options={
                'verbose_name_plural': 'Pojazdy',
            },
        ),
    ]
