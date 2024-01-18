from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
    ]