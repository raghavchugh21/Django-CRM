from django.shortcuts import render, reverse
from leads.forms import LeadModelForm, CustomUserCreationForm
from django.views import generic
from leads.models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LeadListView(LoginRequiredMixin,generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    # def form_valid(self, form):
    #     send_mail(
    #         subject="A lead has been created",
    #         message="Go to the site to see the new lead",
    #         from_email="test@test.com",
    #         recipient_list=["test2@test.com"]
    #     )
    #     return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')
