
from django.urls import path
from applications.views import ApplicationCreateView, ApplicationDeleteView, ApplicationUpdateView, \
    ApplicationStatus2DeleteView, ApplicationStatus1DeleteView, ProductByeCreateView, my_product_read, \
    applications_main, user_read_product, user_bye_product, user_bye_one_product, bye_product_read

app_name = 'applications'
urlpatterns = [


    # path('applications/', ApplicationListView.as_view(), name='applications_read'),
    path('applications/', applications_main, name='applications_read'),
    path('applications/create/', ApplicationCreateView.as_view(), name='applications_create'),
    path('applications-delete/<int:pk>/', ApplicationDeleteView.as_view(), name='applications_delete'),
    path('applications-update/<int:pk>/', ApplicationUpdateView.as_view(), name='applications_update'),
    path('applications-update-status1/<int:pk>/', ApplicationStatus1DeleteView.as_view(), name='applications_update_status1'),
    path('applications-update-status2/<int:pk>/', ApplicationStatus2DeleteView.as_view(), name='applications_update_status2'),
    path('product_bye/<int:pk>/', ProductByeCreateView.as_view(), name='product_bye'),
    path('product_read/', my_product_read, name='product_read'),
    path('user_read_product/', user_read_product, name='user_read_product'),
    path('user_bye_product/<str:user_name>/<str:city>/', user_bye_product, name='user_bye_product'),
    path('user_bye_one_product/<int:id>/', user_bye_one_product, name='user_bye_one_product'),
    # path('product_bye.html/<int:pk>/', product_bye, name='product_bye'),
    path('bye_product_read/', bye_product_read, name='bye_product_read'),

]
