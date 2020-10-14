from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.
#to read the data
class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

#to insert data(create view):
class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')
class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')