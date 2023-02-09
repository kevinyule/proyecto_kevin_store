from django.urls import path
from . import views

urlpatterns = [ 
    path('<pk>', views.ProducDetailview.as_view(), name='product')#id -> llave primaria
]