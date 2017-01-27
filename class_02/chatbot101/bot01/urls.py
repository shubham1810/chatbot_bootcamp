from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.mainBot),
    url(r'^convert', views.convertTemp),
]