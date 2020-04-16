from django.contrib import admin
from django.urls import path

from gym_projec import settings
from pg_adminProduct.views import pg_AdminProduct, InsertProduct, BorrarProduct
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns =[
    path('', pg_AdminProduct.as_view(), name='product_list'),
    path('login/', auth_views.LoginView.as_view(template_name="base/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="base/login.html"), name="logout"),
    path('productos/nuevo', InsertProduct.as_view(), name='insert_product'),
    path('producto/eliminar<int:pk>', BorrarProduct.as_view(), name='delete_product'),
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)