from django.urls import path
from .views import ProductList,ProductDetail, ProductDownloadView

app_name = 'products'

urlpatterns =  [
    path('', ProductList.as_view(), name='list'),
    path('<int:id>/<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('<int:id>/<slug:slug>/download/', ProductDownloadView.as_view(), name='download')
]