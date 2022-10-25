from django.shortcuts import render


def index(request):
    context = {
        'title': 'Работа с заказами', }
    return render(request, 'user_works/index.html', context)
# Create your views here.
