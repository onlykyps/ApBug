from django.urls import path

from aplicatie import views

app_name = 'transactions'

urlpatterns = [
    path('', views.BudgetTransactionView.as_view(), name='transactions_list'),
    path('adaugare/', views.CreateBudgetTransactionView.as_view(), name='adaugare'),
    path('venituri/', views.VenituriView.as_view(), name='venituri'),
    path('raport_venituri/', views.VenituriRaportView.as_view(), name='raport_venituri'),
    path('raport_cheltuieli/', views.CheltuieliRaportView.as_view(), name='raport_cheltuieli'),
]
