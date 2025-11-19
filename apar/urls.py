from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apar_app.views import index, search_order

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('apar_app.urls')),
    path('', index, name='home'),
    path('search/', search_order, name='search'),
]

# Serve media during development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
