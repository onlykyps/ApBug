from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from aplicatie.models import Transaction, BudgetTransaction, VenituriModel


# Create your views here.

class BudgetTransactionView(ListView):
    model = BudgetTransaction
    template_name = 'aplicatie/transactions_index.html'


class CreateBudgetTransactionView(CreateView):
    model = BudgetTransaction
    fields = ['city', 'country']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:transactions_list')


class VenituriView(ListView):
    model = VenituriModel
    template_name = 'aplicatie/Venituri.html'
    pass
