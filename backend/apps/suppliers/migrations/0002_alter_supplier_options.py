# Generated by Django 5.1 on 2024-08-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ('name',)},
        ),
    ]
