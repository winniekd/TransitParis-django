from django.urls import path
from . import views
urlpatterns = [
 path('index/', views.index, name='index'),
 path('show/<int:id_paris>/', views.show, name='show')
]

