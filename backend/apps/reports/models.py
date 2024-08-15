from django.db import models
from apps.products.models import Product, DamagedProduct
from apps.suppliers.models import Supplier
from apps.branches.models import Branch


class ProductInflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity_received = models.PositiveIntegerField()
    manufacturing_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    date_received = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_received',)

    def __str__(self):
        return f"{self.quantity_received} x {self.product.name} from {self.supplier.name}"


class ProductOutflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity_sent = models.PositiveIntegerField()
    expiry_date = models.DateField(null=True, blank=True)
    date_sent = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_sent',)

    def __str__(self):
        return f"{self.quantity_sent} x {self.product.name} to {self.branch.name}"


class InwardQtyReport(models.Model):
    inflow = models.ForeignKey(ProductInflow, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.inflow)


class OutwardQtyReport(models.Model):
    outflow = models.ForeignKey(ProductOutflow, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.outflow)


class ExpiredProductReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} expired on {self.expiry_date}"


class DamagedProductReport(models.Model):
    damaged_product = models.ForeignKey(DamagedProduct, on_delete=models.CASCADE)
    date_reported = models.DateField()

    def __str__(self):
        return f"{self.damaged_product.product.name} reported on {self.date_reported}"


class BranchWiseQtyReport(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} at {self.branch.name}"


class SupplierWiseProductReport(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_supplied = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity_supplied} x {self.product.name} by {self.supplier.name}"
