from django.views.generic import TemplateView, FormView, View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import LoginForm, SensorForm
from .models import Place, Sensor


# Create your views here.
class MqttLogin(FormView):
    template_name = 'iot/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("iot_app:mqtt-dash")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(self.request, user)
            return super(MqttLogin, self).form_valid(form)
        else:
            messages.error(
                self.request,
                "La credenciales ingresadas no son validas. Inténtalo de nuevo.",
            )
            return self.form_invalid(form)


class MqttLogout(LoginRequiredMixin, View):
    def get(self, request, *args, **kargs):
        messages.info(self.request, "Haz cerrado la secion exitosamente.")
        logout(request)
        return HttpResponseRedirect(reverse("core_app:home"))
    

class MqttDashboard(LoginRequiredMixin, FormView):
    template_name = 'iot/dashboard.html'
    login_url = reverse_lazy("iot_app:mqtt-login")
    form_class = SensorForm

    def form_valid(self, form):
        
        place = form.cleaned_data["place"]
        sensor = form.cleaned_data["sensor"]

        url = reverse_lazy(
                "iot_app:mqtt-place-sen",
                kwargs={
                    "place": place.id,
                    "sen": sensor.id,
                },
            )

        return redirect(url)

    

class MqttRecive(LoginRequiredMixin, TemplateView):
    template_name = 'iot/mqtt.html'
    login_url = reverse_lazy("iot_app:mqtt-login")

    def get_context_data(self, **kwargs):
        context = super(MqttRecive, self).get_context_data(**kwargs)
        return context
    
    