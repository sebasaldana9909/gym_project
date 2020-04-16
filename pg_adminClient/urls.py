from django.urls import include,path
from pg_adminClient.views import pg_AdminClient, InsertClient, BorrarClient
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns =[
    path('', pg_AdminClient.as_view(), name='client_list'),
    path('cliente/nuevo', InsertClient.as_view(), name='insert_client'),
    path('cliente/eliminar<int:pk>', BorrarClient.as_view(), name='delete_client'),
]