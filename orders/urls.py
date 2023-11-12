from django.urls import path
from .views import order_create,  payment_completed, payment_canceled, admin_order_detail, admin_order_pdf, stripe_webhook


app_name='orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    # path('process/', payment_process, name='process'),
    path('completed/', payment_completed, name='completed'),
    path('canceled/', payment_canceled, name='canceled'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', admin_order_pdf, name='admin_order_pdf'),
    path('webhook/', stripe_webhook, name='webhook'),
]