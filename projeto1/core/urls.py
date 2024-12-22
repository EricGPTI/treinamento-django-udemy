from django.urls import path
from django.conf.urls import handler404, handler500
from .views import index, contato, produto
from core import views

urlpatterns = [
    path("", index, name='index'),
    path("contato/", contato, name='contato'),
    path("produto/<int:pk>/", produto, name='produto'),
]

handler404 = views.error_404
handler500 = views.error_500
