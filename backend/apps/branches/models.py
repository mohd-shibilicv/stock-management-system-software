from django.db import models
from apps.users.models import User
from apps.products.models import Product


class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    branch_code = models.CharField(max_length=50, unique=True)
    contact_details = models.CharField(max_length=255)
    manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='managed_branch')

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductRequest(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='requests')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_requested',)

    def __str__(self):
        return f"{self.quantity} x {self.product_name} requested by {self.branch.name}"
