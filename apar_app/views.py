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

def bulk_upload(request):
    if request.method == "POST":
        order_ids = request.POST.get("order_ids").split(",")
        order_ids = [oid.strip() for oid in order_ids]

        images = request.FILES.getlist("images")

        for oid, img in zip(order_ids, images):
            Order.objects.create(
                order_id=oid,
                brand_name="Bulk Upload",
                image=img
            )

        return render(request, "bulk_upload.html", {"success": True})

    return render(request, "bulk_upload.html")
