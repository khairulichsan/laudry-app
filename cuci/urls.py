from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_customer, name='home'),
    path('list/', views.index, name='index'),
    path('add/', views.add_order, name='add_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
]
