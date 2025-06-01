from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('products/', views.products, name='products'),
    path('careers/', views.careers, name="careers"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('profile/', views.profile, name='profile'),
    path('order/<str:product_id>/', views.order_product, name='order_product')
]