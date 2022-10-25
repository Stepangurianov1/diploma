from django.urls import path
from user_works.views import index

app_name = 'user_works'
urlpatterns = [

    path('', index, name='works'),

]
