from django.db import models


class InputCustomer(models.Model):
    name = models.CharField(max_length=100)
    nomor_hp = models.CharField(max_length=100)
    alamat = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.nomor_hp}"

class CuciOrder(models.Model):
    SERVICE_CHOICES = [
        ('Cuci Strika', 'Cuci Strika' ),
        ('HandWash', 'HandWash'),
        ('Dry Clean', 'Dry Clean'),
        ('Karpet', 'Karpet'),
    ]

    CUSTOMER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    DEBT_CHOICES = [
        ('Belum Bayar', 'Belum Bayar'),
        ('Lunas', 'Lunas'),
    ]
    
    customer = models.ForeignKey(InputCustomer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    debt = models.CharField(max_length=20, choices=DEBT_CHOICES, default='Belum Bayar')
    status = models.CharField(max_length=20, choices=CUSTOMER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer} - {self.service_type} - {self.status} - {self.debt}"
    
