from django.urls import path
from . import views
from .forms import Transaction
urlpatterns = [
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]