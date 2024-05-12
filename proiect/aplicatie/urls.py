from django.urls import path

from aplicatie import views

app_name = 'transactions'

urlpatterns = [
    path('', views.BudgetTransactionView.as_view(), name='transactions_list'),
    path('adaugare/', views.CreateBudgetTransactionView.as_view(), name='adaugare'),
]
