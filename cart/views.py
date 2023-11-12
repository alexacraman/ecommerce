from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
import json
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product)
    cart_len = cart.__len__()
    cart_cost = cart.get_total_price()
    response_data = {
        "cart_count": cart_len,
        "cart_cost": cart_cost
    }
    return JsonResponse({'data': response_data})
    

def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product=product)
    cart_len = cart.__len__()
    cart_cost = cart.get_total_price()
    response_data = {
        "cart_count": cart_len,
        "cart_cost":  cart_cost
    }
    return JsonResponse({'data': response_data}, safe=False)
 
def cart_detail(request):
    cart = Cart(request)
    cart_items = cart.__iter__()  
    total_price = cart.get_total_price()  
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

def cart_object(request):
    cart = Cart(request)
    cart_items = cart.__iter__()
    cart_items_list = []
    for item in cart_items:
        cart_items_list.append({
            'product': item['product'].name,
            'quantity': item['quantity'],
            'price': item['price'],
            'total': item['price'] * item['quantity']
        })
    response_data = {
        'cart_items': cart_items_list, 
    }
    return JsonResponse(response_data)

    
    # return JsonResponse({'data': data}, safe=False)
    

# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
#     return redirect('cart:cart_detail')

# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('products:list')

# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override':True}) 
#     return render(request, 'cart/cart_detail.html', {'cart': cart})