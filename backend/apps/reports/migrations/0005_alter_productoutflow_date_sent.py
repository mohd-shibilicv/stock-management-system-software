# Generated by Django 5.1 on 2024-08-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_productinflow_date_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoutflow',
            name='date_sent',
            field=models.DateField(auto_now_add=True),
        ),
    ]
