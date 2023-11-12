from django.urls import path
from .views import dashboard, user_orders, delete_account

app_name = 'accounts'


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('user_orders/', user_orders, name='user_orders'),
    path('delete_account/', delete_account, name='delete_account')
]