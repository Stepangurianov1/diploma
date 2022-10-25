from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from applications.models import MyProductsModel, ApplicationModel
from cart.cart import Cart
from mainapp.models import Product_for_diller, Product


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        for item in cart:
            name_application = ApplicationModel.objects.filter(
                name=item['product'].name).first()
            obj, created = MyProductsModel.objects.get_or_create(user_name=request.user,
                                                                 model=item['product'],
                                                                 name_application=name_application,
                                                                 )
            if created:
                obj.quantity = item['quantity']
                obj.price = item['price']
            else:
                obj.quantity += item['quantity']
                obj.price += item['price']
            obj.save()
            if request.user.user_role == 'Дилер':
                all_quantity = Product_for_diller.objects.get(name=Product.objects.get(name=item['name']),
                                                              model=item['model'])
                all_quantity.quantity -= item['quantity']
                all_quantity.save()
            if request.user.user_role == 'Пользователь':
                pass
            # print(item)
        cart.clear()
        messages.success(request, 'Вы успешно преобреи товар, корзина пуста')
        return HttpResponseRedirect(reverse('cart:cart_detail'))
    return HttpResponseRedirect(reverse('cart:cart_detail'))
