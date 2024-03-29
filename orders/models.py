from django.db import models
from django.conf import settings
from product.models import Product

class Order(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_user")
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    email       = models.EmailField()
    address     = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    paid        = models.BooleanField(default=False)
    stripe_id   = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def get_stripe_url(self):
        if not self.stripe_id:
            # no payment associated
            return ''
        if '_test_' in settings.STRIPE_API_KEY_HIDDEN:
            # Stripe path for test payments
            path = '/test/'
        else:
            # Stripe path for real payments
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'

class OrderItem(models.Model):
    order       = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product     = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price       = models.DecimalField(max_digits=10,decimal_places=2)
    quantity    = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


