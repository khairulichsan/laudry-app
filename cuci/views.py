from django.shortcuts import render, redirect
from .models import CuciOrder
from .forms import CuciOrderForm

def index(request):
    orders = CuciOrder.objects.all()
    return render(request, 'cuci/index.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = CuciOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CuciOrderForm()
    return render(request, 'cuci/add_order.html', {'form': form})

def delete_order(request, order_id):
    order = CuciOrder.objects.get(id=order_id)
    order.delete()
    return redirect('index')
