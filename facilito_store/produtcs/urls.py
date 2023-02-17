from django.urls import path
from . import views

urlpatterns = [ 
    path('<slug:slug>', views.ProducDetailview.as_view(), name='product')#id -> llave primaria
]