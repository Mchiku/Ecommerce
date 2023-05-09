# Generated by Django 4.2 on 2023-04-23 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Baragoi', 'Baragoi'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Butere', 'Butere'), ('dadaab', 'dadaab'), ('Diani Beach', 'Diani Beach'), ('Eldoret', 'Eldoret'), ('Email', 'Email'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Gede', 'Gede'), ('Hola', 'Hola'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kitui', 'Kitui'), ('Kibwezi', 'Kibwezi'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kakuma', 'Kakuma'), ('Kapenguria', 'Kapenguria'), ('kericho', 'Kericho'), ('Keroka', 'Keroka'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitale', 'Kitale'), ('Lamu', 'Lamu'), ('Langata', 'Langata'), ('Litein', 'Litein'), ('Lodwar', 'Lodwar'), ('Lokichoggio', 'Lokichoggio'), ('Londiani', 'Londiani'), ('Loyangalani', 'Loyangalani'), ('Machakos', 'Machakos'), ('Makindu', 'Makindu'), ('Malindi', 'Malindi'), ('Mandera', 'Mandera'), ('Maralal', 'Maralal'), ('Marsabit', 'Marsabit'), ('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Moyale', 'Moyale'), ('Mumias', 'Mumias'), ('Muranga', 'Muranga'), ('Mutomo', 'Mutomo'), ('Nairobi', 'Nairobi'), ('Naivasha', 'Naivasha'), ('Nakuru', 'Nakuru'), ('Namanga', 'Namanga'), ('Nanyuki', 'Nanyuki'), ('Naro Moru', 'Naro Moru'), ('Narok', 'Narok'), ('Nyahururu', 'Nyahururu'), ('Nyeri', 'Nyeri'), ('Ruiru', 'Ruiru'), ('Shimoni', 'Shimoni'), ('Takaungu', 'Takungu'), ('Thika', 'Thika'), ('Vihiga', 'Vihiga'), ('Voi', 'Voi'), ('Wajir', 'Wajir'), ('Watamu', 'Watamu'), ('Webuye', 'Webuye'), ('Wote', 'Wote'), ('Wundanyi', 'Wundanyi')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
