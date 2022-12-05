from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.greetings, name='greetings'),
    path('', views.list_item, name='items'),
    path('<int:id>', views.detail_item, name='detail'),
]

