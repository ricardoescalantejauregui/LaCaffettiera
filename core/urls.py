from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    # path('contact/', views.contact, name='contact'),
    # path('blog/', views.blog, name='blog'),
    # path('sample/', views.sample, name='sample'),

]
