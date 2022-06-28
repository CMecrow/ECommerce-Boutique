from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LFaNIBz28O6pWUISi9TS4UpSK6gzHQ6RVXDogvr4NknW0YcoAdplp1lSC6QHdHO8dvbfCXWQ3enWC3z4BemeCDd00TFgjRLnC',
    }

    return render(request, template, context)