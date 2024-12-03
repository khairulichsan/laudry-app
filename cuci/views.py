from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import CuciOrder
from .models import InputCustomer
from .forms import CuciOrderForm


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def index(request):
    orders = CuciOrder.objects.all()
    return render(request, 'cuci/index.html', {'orders': orders})


@login_required
@user_passes_test(is_admin)
def add_order(request):
    if request.method == 'POST':
        form = CuciOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CuciOrderForm()
    return render(request, 'cuci/add_order.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_order(request, order_id):
    order = get_object_or_404(CuciOrder,id=order_id)
    order.delete()
    return redirect('index')


def search_customer(request):
    nomor_hp = request.GET.get('nomor_hp')  # Ambil nomor HP dari form
    orders = None

    if nomor_hp:
        try:
            # Cari customer berdasarkan nomor HP
            customer = InputCustomer.objects.get(nomor_hp=nomor_hp)
            # Ambil semua riwayat order untuk customer tersebut
            orders = CuciOrder.objects.filter(customer=customer)
        except InputCustomer.DoesNotExist:
            orders = None

    return render(request, 'home.html', {
        'nomor_hp': nomor_hp,
        'orders': orders,
    })

def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')