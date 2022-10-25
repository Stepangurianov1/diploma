from django import forms

from applications.models import ApplicationModel, MyProductsModel
from mainapp.models import Product


class ApplicationForm(forms.ModelForm):
    class Meta(object):
        model = ApplicationModel
        fields = ('user_name', 'name', 'city', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ApplicationUpdateForm(forms.ModelForm):
    class Meta(object):
        model = ApplicationModel
        fields = ('name', 'city', 'description')

    def __init__(self, *args, **kwargs):
        super(ApplicationUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        # self.object.quantity += instance.quantity
        # self.object.save()

        # form.instance.testing += self.object.testing
        # my_object = MyProductsModel.objects.get_or_create(pk=self.kwargs.get('pk'), model=instance.model)
        # my_object = MyProductsModel.objects.filter(model=instance.model)
        # if my_object.first() is not None:
class ProductBye(forms.ModelForm):
    class Meta(object):
        model = MyProductsModel
        fields = ( 'model', 'quantity')

    def __init__(self, *args, **kwargs):
        super(ProductBye, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
