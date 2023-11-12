from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from orders.models import Order, OrderItem
from product.models import Product
from .forms import DeleteUserForm

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {})

@login_required
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(paid=True)
    return render(request, "account/user_orders.html", {"orders": orders})


def delete_account(request):
    if request.method == "POST":
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            if request.POST['delete_checkbox']:
                user_obj = User.objects.get(email=request.user)
                if user_obj is not None:
                    user_obj.delete()
                    logout(request)
                    messages.warning(request, 'You have deleted your account')
                    return redirect('accounts:signup')
                else:
                    messages.info(request, 'There was a problem deleting your account.')

    else:
        form = DeleteUserForm()
        return render(request, 'account/delete_acc.html', {'form': form})