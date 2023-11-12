from django.urls import path
from .views import cart_add, cart_detail, cart_remove, cart_object

app_name = 'cart'


urlpatterns = [
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('items/', cart_detail, name='cart_detail'),
    path('items/data/', cart_object, name='cart-object')
]