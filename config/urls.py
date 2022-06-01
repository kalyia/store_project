from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('apps.product.urls')),
    path('account/', include('apps.product.urls')),
    path('category/', include('apps.product.urls')),
]
