# Generated by Django 4.1.1 on 2023-08-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeScreen', '0003_alter_eğitimler_tarih'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kadro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('meslek', models.CharField(max_length=100)),
                ('aciklama', models.TextField(max_length=500)),
                ('resim', models.FileField(blank=True, null=True, upload_to='kadrolar')),
            ],
        ),
    ]
