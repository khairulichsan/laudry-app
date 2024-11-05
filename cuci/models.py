from django.db import models

class CuciOrder(models.Model):
    CUSTOMER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    DEBT_CHOICES = [
        ('Belum Bayar', 'Belum Bayar'),
        ('Lunas', 'Lunas'),
    ]
    
    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    debt = models.CharField(max_length=20, choices=DEBT_CHOICES, default='Belum Bayar')
    status = models.CharField(max_length=20, choices=CUSTOMER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.service_type} - {self.status} - {self.debt}"