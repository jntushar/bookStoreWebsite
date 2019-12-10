from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newarrivals/', views.newarrivals, name='newarrivals'),
    path('blog/', views.blog, name='blog'),
    path('contactus/', views.contactus, name='contactus'),
    path('quickview/<int:myid>', views.quickview, name='quickview'),
    path('search/', views.search, name='search'),
    path('deliverydetails/', views.deliverydetails, name='deliverydetails'),
    path('thankyou/', views.thankyou, name='thankyou'),
]


