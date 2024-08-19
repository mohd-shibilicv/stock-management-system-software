# Generated by Django 5.1 on 2024-08-19 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0006_alter_branch_branch_code'),
        ('products', '0005_product_barcode_image_alter_product_opening_stock'),
        ('reports', '0006_alter_productinflow_supplier'),
        ('suppliers', '0002_alter_supplier_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damagedproductreport',
            name='damaged_product',
        ),
        migrations.RemoveField(
            model_name='expiredproductreport',
            name='product',
        ),
        migrations.RemoveField(
            model_name='inwardqtyreport',
            name='inflow',
        ),
        migrations.RemoveField(
            model_name='outwardqtyreport',
            name='outflow',
        ),
        migrations.RemoveField(
            model_name='supplierwiseproductreport',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplierwiseproductreport',
            name='supplier',
        ),
        migrations.AlterField(
            model_name='productinflow',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productinflow', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productinflow',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productinflow', to='suppliers.supplier'),
        ),
        migrations.AlterField(
            model_name='productoutflow',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productoutflow', to='branches.branch'),
        ),
        migrations.AlterField(
            model_name='productoutflow',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productoutflow', to='products.product'),
        ),
        migrations.DeleteModel(
            name='BranchWiseQtyReport',
        ),
        migrations.DeleteModel(
            name='DamagedProductReport',
        ),
        migrations.DeleteModel(
            name='ExpiredProductReport',
        ),
        migrations.DeleteModel(
            name='InwardQtyReport',
        ),
        migrations.DeleteModel(
            name='OutwardQtyReport',
        ),
        migrations.DeleteModel(
            name='SupplierWiseProductReport',
        ),
    ]
