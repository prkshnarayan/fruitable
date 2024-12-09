from django.urls import path

from fruitapp import views

urlpatterns = [
    path('', views.home),
    path('shop/', views.shop),
    path('shop-detail/', views.shop_detail),
    path('cart/', views.cart),
    path('chackout/', views.chackout),
    path('testimonial/', views.testimonial),
    path('404/', views.error404),
    path('contact/', views.contact),
]