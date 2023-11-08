from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('booktrip/', include('booktrip.urls')),
    path('contactus/', include('contactus.urls')),
    path('charterbus/', include('charterbus.urls')),
    path('faq/', include('faq.urls')),
    path('login/', include('login.urls')),
    path('privacypolicy/', include('privacypolicy.urls')),
    path('register/', include('register.urls')),
    path('schedules/', include('schedules.urls')),
    path('safety/', include('safety.urls')),
    path('shipping/', include('shipping.urls')),
    path('termsconditions/', include('termsconditions.urls')),
    path('tickets/', include('tickets.urls')),
    path("admin/", admin.site.urls),
]
