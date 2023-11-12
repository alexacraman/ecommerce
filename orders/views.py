from io import BytesIO
import weasyprint
from django.contrib import messages
from django.template.loader import render_to_string
import stripe
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],quantity=item['quantity'], price=item['price'])
            success_url = request.build_absolute_uri(
            reverse('orders:completed')
            )
            cancel_url = request.build_absolute_uri(
                reverse('orders:canceled')
            )
            session_data = {
                'mode': 'payment',
                'success_url': success_url,
                'cancel_url': cancel_url,
                'line_items': []
            }
            for item in order.items.all():
                session_data['line_items'].append({
                    'name': item.product.name,
                    'amount': int(item.price * Decimal('100')),
                    'currency': 'gbp',
                    'quantity': item.quantity,
                })
            session = stripe.checkout.Session.create(**session_data)
            order.stripe_id = session.payment_intent
            order.save()
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(session.url, code=303)
           
    else:
        form = OrderCreateForm()
    return render(request, 'order/order_create.html', {'cart': cart, 'form': form})
    

def payment_completed(request):
    return render(request, 'order/completed.html')

def payment_canceled(request):
    return render(request, 'order/canceled.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
                    payload,
                    sig_header,
                    settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        if session['mode'] == 'payment':
            payment_intent_id = session['payment_intent']
            try:
                order = Order.objects.get(stripe_id=payment_intent_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # mark order as paid
            order.paid = True
            order.save()
            # launch asynchronous task
            # payment_completed.delay(order.id)

    return HttpResponse(status=200)

# stripe login
# stripe listen --forward-to localhost:8000/orders/webhook/

def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject =   f'Order number {order.id}'
    message =   f'Dear {order.first_name},\n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'eoceanweb@gmail.com', [order.email])
    return mail_sent

# def payment_completed(order_id):
#     order = Order.objects.get(id=order_id)
#     subject = f'MHA = Invoice no. {order.id}'
#     message = 'Please find attached the invoice for your recent purchase'
#     email = EmailMessage(subject, message, 'eoceanweb@gmail.com',[order.email])
#     html = render_to_string('order/pdf.html', {'order':order})
#     out = BytesIO()
#     stylesheets=[weasyprint.CSS(filename= 'static/css/pdf.css')]
#     weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
#     email.attach(f'order{order.id}.pdf',
#     out.getvalue(),'application/pdf')
#     email.send()



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(filename = 'static/css/pdf.css')])
        
    return response







# def payment_process(request):
#     order_id = request.session.get('order_id', None)
#     order = get_object_or_404(Order, id=order_id)

#     if request.method == "POST":
#         success_url = request.build_absolute_uri(
#             reverse('order:completed')
#         )
#         cancel_url = request.build_absolute_uri(
#             reverse('order:canceled')
#         )
#         session_data = {
#             'mode': 'payment',
#             'success_url': success_url,
#             'cancel_url': cancel_url,
#             'line_items': []
#         }
#         for item in order.items.all():
#             session_data['line_items'].append({
#                 'name': item.product.name,
#                 'amount': int(item.price * Decimal('100')),
#                 'currency': 'gbp',
#                 'quantity': item.quantity,
#             })
#         session = stripe.checkout.Session.create(**session_data)
#         order.stripe_id = session.payment_intent
#         order.save()

#         return redirect(session.url, code=303)
#     else:
#         return render(request, 'order/process.html')