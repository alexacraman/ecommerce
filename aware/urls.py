from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import contact_view, priv_pol,landing

from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap, StaticSitemap

sitemaps = {
    'static': StaticSitemap,
    'blog': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('contact/', contact_view, name='contact_view'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('product.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('stats/', include('stats.urls', namespace='stats')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('policy/', priv_pol, name='policy'),
    
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
