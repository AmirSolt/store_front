from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    
    path('info/explore', views.explore, name='explore'),
    
    
    path('auth/choose_username', views.choose_username, name='choose_username'),


    path('payment/checkout', views.checkout, name='checkout'),


    path('s/<str:username>', views.store_page, name='store_page'),
    path('s/<str:username>/edit', views.store_edit, name='store_edit'),
    path('s/<str:username>/edit/links', views.store_edit_links, name='store_links'),


    path('p/<str:username>/add_products', views.add_products, name='add_products'),

]