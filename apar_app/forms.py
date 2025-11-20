from django import forms
from .models import Order

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'brand_name', 'image']

class BulkUploadForm(forms.Form):
    images = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True}),
        required=True
    )
    order_ids = forms.CharField(required=True)

