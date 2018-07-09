from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.dashboard),
    url(r'^books/add$', views.books),
    url(r'^user/(?P<id>\d+)$', views.showUser),
    url(r'^comment$', views.addComment),
]