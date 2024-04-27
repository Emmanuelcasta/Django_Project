from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, Product # Modificado

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Modificado
    path('about/', AboutPageView.as_view(), name='about'),  # Modificado
    path('contact/', ContactPageView.as_view(), name='contact'),  # Modificado
    path('products/', ProductIndexView.as_view(), name='index'),  # Modificado
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),

]
