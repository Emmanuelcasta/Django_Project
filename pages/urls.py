from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView  # Modificado

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Modificado
    path('about/', AboutPageView.as_view(), name='about'),  # Modificado
    path('contact/', ContactPageView.as_view(), name='contact'),  # Modificado
    path('products/', ProductIndexView.as_view(), name='products'),  # Modificado
    path('products/<int:id>/', ProductShowView.as_view(), name='product_show'),  # Modificado
]
