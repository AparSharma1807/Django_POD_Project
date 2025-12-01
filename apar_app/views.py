from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from .forms import BulkUploadForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, "POD Uploaded Successfully!") # ← Add here
            return redirect('home')
        # redirect to clear POST
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
            # return redirect('search')

    return render(request, 'search.html', {
        'query': query,
        'result': result,
    })

def bulk_upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        # Loop through all uploaded images
        for index, image in enumerate(images):
            # Get order IDs for THIS image
            key = f"order_ids_for_image_{index}"
            order_ids = request.POST.get(key, "")

            if not order_ids.strip():
                continue  # skip if empty
            
            order_list = [o.strip() for o in order_ids.split(",") if o.strip()]

            # Save one database row per order ID
            for order_id in order_list:
                Order.objects.create(
                    order_id=order_id,
                    brand_name="",
                    image=image
                )
        messages.success(request, "PODs Uploaded Successfully!")
        return redirect("bulk_upload")
    return render(request, "bulk_upload.html")
