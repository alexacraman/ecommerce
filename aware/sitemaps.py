from django.contrib.sitemaps import Sitemap
from product.models import Product
from django.urls import reverse


class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created

class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.3

    def items(self):
        return ['contact_view', 'policy']

    def location(self, item):
        return reverse(item)