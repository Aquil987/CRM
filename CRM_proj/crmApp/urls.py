from django.urls import path
from . import views
urlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('customer_record/<int:pk>', views.customer_record, name='customer_record'),
    path('update_cutomer/<int:pk>', views.update_cutomer, name='update_cutomer'),
    path('delete_cutomer/<int:pk>', views.delete_cutomer, name='delete_cutomer'),
    path('add_record/', views.add_record, name='add_record'),

]