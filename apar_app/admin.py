from django.contrib import admin
from .models import Order

admin.site.site_header = "Apar's Administration"
admin.site.site_title = "Apar's Admin Panel"
admin.site.index_title = "Welcome to Apar's Dashboard"

admin.site.register(Order)
