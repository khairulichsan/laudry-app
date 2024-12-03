from django.contrib import admin

# Register your models here.
from .models import InputCustomer
from .models import CuciOrder

@admin.register(InputCustomer)
class InputCustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'nomor_hp']  # Menambahkan pencarian berdasarkan nama dan nomor HP
    list_display = ['name', 'nomor_hp', 'alamat']  # Tampilkan field-field ini di daftar admin


# Konfigurasi untuk CuciOrder agar field customer mendukung autocomplete
@admin.register(CuciOrder)
class CuciOrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']  # Aktifkan autocomplete pada field customer
    list_display = ['customer', 'service_type', 'price', 'status', 'debt']  # Tampilkan field-field ini di daftar admin
    list_filter = ['status', 'debt']  # Tambahkan filter untuk status dan debt