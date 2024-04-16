from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Modificado
    path('about/', AboutPageView.as_view(), name='about'),  # Modificado
    path('contact/', ContactPageView.as_view(), name='contact'),  # Modificado
]
