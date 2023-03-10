
from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views
from produtcs.views import productListView

urlpatterns = [
    path('', productListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('produtcs.urls'))

]
