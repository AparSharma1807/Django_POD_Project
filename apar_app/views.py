from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')   # redirect to clear POST
    else:
        form = OrderForm()

    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'form': form, 'orders': orders})

def search_order(request):
    query = request.GET.get('order_id')
    result = None

    if query:
        try:
            result = Order.objects.get(order_id__iexact=query)
        except Order.DoesNotExist:
            result = "notfound"

    return render(request, 'search.html', {
        'query': query,
        'result': result,
    })