# Generated by Django 4.1.1 on 2023-08-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeScreen', '0005_kadro_linkedn'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadro',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kadro',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
