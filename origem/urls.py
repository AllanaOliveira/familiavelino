from django.conf.urls.static import static
from django.urls import path, include

from origem import views

app_name = 'origem'

urlpatterns = [
    path('', views.origem, name='origem'),
]