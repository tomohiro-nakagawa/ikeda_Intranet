from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (ListView 
                                  ,DetailView 
                                  ,FormView
                                 )
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import NippoModel
from .forms  import NippoFormClass, NippoModelForm
from django.urls import reverse, reverse_lazy,path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from utils.access_restrictions import OwnerOnly
from .filters import  NippoModelFilter
from accounts.models import Profile

class NippoListView(ListView): #クラス作成
    template_name = "nippo/nippo-list.html" #変数
    model = NippoModel #変数

    def get_queryset(self):
        q = self.request.GET.get("search")
        return NippoModel.objects.search(query=q)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter"] = NippoModelFilter(self.request.GET, queryset=self.get_queryset())
        profile_id = self.request.GET.get("profile")
        q = Profile.objects.filter(id=profile_id)
        if q.exists():
            ctx["profile"] = q.first()
        return ctx

class NippoDetailView(DetailView):
    template_name = "nippo/nippo-detail.html"
    model = NippoModel

class NippoCreateModelFormView(LoginRequiredMixin, CreateView):
    template_name = "nippo/nippo-form.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
    def get_form_kwargs(self, *args, **kwargs):
        kwgs = super().get_form_kwargs(*args, **kwargs)
        kwgs["user"] = self.request.user
        return kwgs

class NippoUpdateModelFormView(OwnerOnly,UpdateView):
    template_name = "nippo/nippo-form.html"
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")

class NippoDeleteView(OwnerOnly,DeleteView):
    template_name = "nippo/nippo-delete.html"
    model = NippoModel
    success_url = reverse_lazy("nippo-list")

def Nippo0View(request): #クラス作成
    return render(request,"nippo/nippo-0.html")

def Nippo11View(request): #クラス作成
    return render(request,"nippo/nippo-1-1.html")

def Nippo12View(request): #クラス作成
    return render(request,"nippo/nippo-1-2.html")

def Nippo13View(request): #クラス作成
    return render(request,"nippo/nippo-1-3.html")

def Nippo14View(request): #クラス作成
    return render(request,"nippo/nippo-1-4.html")

def Nippo15View(request): #クラス作成
    return render(request,"nippo/nippo-1-5.html")

def Nippo21View(request): #クラス作成
    return render(request,"nippo/nippo-2-1.html")

def Nippo22View(request): #クラス作成
    return render(request,"nippo/nippo-2-2.html")

def Nippo23View(request): #クラス作成
    return render(request,"nippo/nippo-2-3.html")

def Nippo3View(request): #クラス作成
    return render(request,"nippo/nippo-3.html")

def Nippo4View(request): #クラス作成
    return render(request,"nippo/nippo-4.html")
