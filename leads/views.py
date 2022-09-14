
from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import LeadForm
from django.views.generic import TemplateView, DeleteView, ListView, DetailView, CreateView, UpdateView

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list_view(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

class LeadDetailView(DetailView):
    template_name = "leads/lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail_view(request, pk):
    lead = Lead.objects.get(id=pk)
    context= {
        "lead":lead
    }
    return render(request, "leads/lead_details.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_create_view(request):
    form = LeadForm()
    
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
        
    context = {
            "form":form
        }

    return render(request, "leads/lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_update_view(request,pk):
    
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
        
    context = {
            "form":form,
            "lead":lead
        }

    return render(request, "leads/lead_update.html", context)

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_delete_view(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")