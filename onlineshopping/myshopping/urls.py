from django.contrib import admin
from django.urls import path
from myshopping import views
from django.conf.urls import url, include
from . import views
from .views import SearchResultsView, BootstrapFilterView
from accounts.views import login_view, register_view, logout_view, delete_profile
from cart.views import CartView, add_to_cart, remove_from_cart, checkout, clearCart
from myshopping.views import products
from myshopping import urls

urlpatterns = [

    path('', views.Data_list, name='sublist'),
    path('products/', products, name='products'),
    path('productbyname/<productName>/', views.displayProductData, name='productbyname'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', views.BootstrapFilterView, name='search_results'),
    path('accounts/login/', login_view),
    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view),
    path('accounts/delete/', delete_profile),
    path('products/cart/<product_name>', add_to_cart, name='cart'),
    path('products/remove/<product_name>', remove_from_cart, name='remove-cart'),
    path('products/cartview/', CartView, name='cart-home'),
    path('productbyname/cart/<product_name>', add_to_cart, name='cart'),
    path('products/cartview/remove/<product_name>', remove_from_cart, name='remove-cart'),
    path('checkout', checkout, name='checkout'),
    path('products/cartview/checkout/clearCart', clearCart, name='clearcart'),

]
