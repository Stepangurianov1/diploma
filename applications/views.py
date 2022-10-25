from email._header_value_parser import Section

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView, TemplateView
# Create your views here.
from pyexpat.errors import messages
from django import forms
from applications.forms import ApplicationForm, ApplicationUpdateForm, ProductBye
from applications.models import ApplicationModel, MyProductsModel
from authapp.models import User
from cart.form import CartAddProductForm
from mainapp.admin import Product
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin

# class ApplicationListView(ListView, BaseClassContextMixin):
#     model = ApplicationModel
#     template_name = 'applications/applications-read.html'
#     title = 'Сформированные заявки'
from mainapp.models import Product_for_diller


def applications_main(request):
    if request.user.user_role == 'Сотрудник':
        applications = ApplicationModel.objects.all()
    else:
        applications = ApplicationModel.objects.filter(user_name=request.user)
    context = {'applications': applications}
    return render(request, 'applications/applications-read.html', context)


class ApplicationStatus1DeleteView(DeleteView, BaseClassContextMixin):
    model = ApplicationModel
    template_name = 'applications/applications-update-delete.html'
    success_url = reverse_lazy('applications:applications_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = 'Отклонено'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ApplicationStatus2DeleteView(DeleteView, BaseClassContextMixin):
    model = ApplicationModel
    template_name = 'applications/applications-update-delete.html'
    success_url = reverse_lazy('applications:applications_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = 'Одобрено'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ApplicationCreateView(CreateView, BaseClassContextMixin):
    model = ApplicationModel
    template_name = 'applications/applications-create.html'
    form_class = ApplicationUpdateForm
    # permission_required = 'news.add_post'
    success_url = reverse_lazy('applications:applications_read')
    title = 'Формирование заявки'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_name = self.request.user

        super().form_valid(form)
        instance.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductByeCreateView(CreateView):
    model = MyProductsModel
    template_name = 'applications/product_bye.html'
    form_class = ProductBye
    success_url = reverse_lazy('applications:applications_read')

    def get_context_data(self, **kwargs):
        application = ApplicationModel.objects.filter(pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context["applications"] = application
        return context

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        instance.name_application = ApplicationModel.objects.get(pk=self.kwargs.get('pk'))
        instance.user_name = self.request.user
        objs = MyProductsModel.objects.filter(name_application=instance.name_application, model=instance.model)
        obj_dealer = Product_for_diller.objects.get(model=instance.model)
        obj_dealer.quantity -= instance.quantity
        if obj_dealer.quantity > 0:
            obj_dealer.save()
        else:
            obj_dealer.delete()
        if objs:
            obj = objs.first()
            print(obj.name_application.user_name)
            obj.quantity += instance.quantity
            obj.save()
            return HttpResponseRedirect(reverse('applications:applications_read'))
        super().form_valid(form)
        instance.save()
        return HttpResponseRedirect(self.get_success_url())


# class MyProductsListView(ListView, BaseClassContextMixin):
#     model = MyProductsModel
#     queryset = MyProductsModel.objects.filter(name_application='Продажа ноутбуков')
#     template_name = 'applications/read_my_product.html'
#     title = 'Мой склад'


def my_product_read(request):
    # name_applications = ApplicationModel.objects.filter(user_name=request.user)
    # print(name_applications)
    products = MyProductsModel.objects.filter(user_name=request.user)
    context = {'object_list': products}
    return render(request, 'applications/read_my_product.html', context)


def bye_product_read(request):
    applications = ApplicationModel.objects.filter(user_name=request.user, is_active='Одобрено')
    products = []
    for application in applications:
        products.extend(list(Product_for_diller.objects.filter(name=application.name)))
    cart_product_form = CartAddProductForm()
    context = {'products': products, 'cart_product_form': cart_product_form}
    return render(request, 'applications/bye_product_read.html', context)


def user_read_product(request):
    products = ApplicationModel.objects.filter(is_active='Одобрено', user_name__user_role='Дилер')
    context = {'products': products}
    return render(request, 'applications/user_read_city.html', context)


def user_bye_product(request, user_name, city):
    products = MyProductsModel.objects.filter(user_name__username=user_name)
    # , name_application__city=city добавить в фильтр
    cart_product_form = CartAddProductForm()
    context = {'products': products, 'cart_product_form': cart_product_form}
    return render(request, 'applications/user_bye_products.html', context)


def user_bye_one_product(request, id):
    product = MyProductsModel.objects.get(id=id)
    my_product = MyProductsModel.objects.get_or_create(user_name=request.user,
                                                       name_application=product.name_application,
                                                       model=product.model)
    # my_product.quantity = 1
    # cart_product_form = CartAddProductForm()
    product.quantity -= 1
    # my_product.save()
    product.save()
    return HttpResponseRedirect(reverse('applications:user_read_product'))


class ApplicationDeleteView(DeleteView):
    model = ApplicationModel
    template_name = 'applications/applications-update-delete.html'
    success_url = reverse_lazy('applications:applications_read')


class ApplicationUpdateView(UpdateView, BaseClassContextMixin):
    model = ApplicationModel
    template_name = 'applications/applications-update-delete.html'
    form_class = ApplicationUpdateForm
    title = 'Обновление заявки'
    success_url = reverse_lazy('applications:applications_read')
