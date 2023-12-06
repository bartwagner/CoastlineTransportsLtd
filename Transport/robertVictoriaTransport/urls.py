from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('booktrip/', include('booktrip.urls')),
    path('charterbus/', include('charterbus.urls')),
    path('contactus/', include('contactus.urls')),
    path('information/', include('information.urls')),
    path('shipping/', include('shipping.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
