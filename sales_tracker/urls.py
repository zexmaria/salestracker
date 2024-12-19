from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('sales_tracker.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('', include('sales_tracker.core.urls')),
]
