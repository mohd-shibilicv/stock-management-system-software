# Generated by Django 5.1 on 2024-08-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0004_remove_productrequest_fulfilled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchproduct',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10),
        ),
    ]
