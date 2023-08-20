from django.urls import path
from . import views #import all the views from this directory

urlpatterns = [
    path('',views.store,name='store'),
    path('login/', views.login_view,name='login'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
]