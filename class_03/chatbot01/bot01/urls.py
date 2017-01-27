from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^data/', views.showData),
]
