from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from aplicatie.models import Transaction, BudgetTransaction, VenituriModel, CheltuieliRaportModel, CheltuieliModel


# Create your views here.

# sectiune cod inutil de la teste

class BudgetTransactionView(ListView):
    model = BudgetTransaction
    template_name = 'aplicatie/transactions_index.html'


# sectiune cod inutil de la teste


# sectiune cod util
class CreateBudgetTransactionView(CreateView):
    model = CheltuieliModel
    fields = ['city', 'country']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:cheltuieli')


class CheltuieliView(ListView):
    model = CheltuieliModel
    template_name = 'aplicatie/cheltuieli.html'


class VenituriView(ListView):
    model = VenituriModel
    template_name = 'aplicatie/Venituri.html'
    pass


class VenituriRaportView(ListView):
    model = VenituriModel
    template_name = 'aplicatie/raport_venituri.html'
    pass


class CheltuieliRaportView(ListView):
    model = CheltuieliRaportModel
    template_name = 'aplicatie/raport_cheltuieli.html'
    pass
