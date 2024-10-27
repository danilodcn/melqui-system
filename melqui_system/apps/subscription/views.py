from django.forms import ModelForm
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from melqui_system.apps.subscription.forms import RegistrationSubscriptionForm


class RegistrationView(generic.FormView):
    template_name = 'subscription.html'
    form_class = RegistrationSubscriptionForm
    success_url = '/thanks'

    def get_success_url(self) -> str:
        return reverse('registration-thanks', kwargs={'id': self.object.id})

    def form_valid(self, form: ModelForm) -> HttpResponse:
        self.object = form.save()
        return super().form_valid(form)


class RegistrationSuccessView(generic.TemplateView):
    template_name = 'thanks.html'
