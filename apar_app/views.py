from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from .forms import BulkUploadForm

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
        images = request.FILES.getlist('images')
        order_ids = request.POST.get('order_ids')

        # Split comma-separated order IDs
        order_list = [o.strip() for o in order_ids.split(",")]

        # Check if order_ids count matches image count
        if len(order_list) != len(images):
            return render(request, "bulk_upload.html", {
                "error": "Number of images must match with number of order IDs."
            })

        # Save each image with its order ID
        for order_id, image in zip(order_list, images):
            Order.objects.create(
                order_id=order_id,
                brand_name="",    # or remove this field if not required
                image=image
            )

        return render(request, "bulk_upload.html", {
            "success": True
        })

    return render(request, "bulk_upload.html")