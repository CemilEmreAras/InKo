# Generated by Django 4.1.1 on 2023-08-13 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeScreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eğitimler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('aciklama', models.TextField(max_length=400)),
                ('fiyat', models.IntegerField()),
                ('resim', models.FileField(blank=True, null=True, upload_to='urunler/', verbose_name='Ürün Resmi')),
                ('tarih', models.IntegerField()),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homeScreen.kategori')),
            ],
        ),
        migrations.DeleteModel(
            name='Urun',
        ),
    ]
