from django.shortcuts import render

# Create your views here.
import datetime

from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Vehicle, Action
#from .models import Zawody, Zawodnik, Klub, Zekken, KategoriaKata, KategoriaKumite
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
#from .forms import ZmianaZawodowForm, ZawodnikSubmitForm, ZawodnikCreateForm, KlubSubmitForm, ZekkenCreateForm
from .forms import ActionCreateForm, VehicleSubmitForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    # Generate counts of some of the main objects
    num_vehicle = Vehicle.objects.all().count()
    num_action = Action.objects.all().count()

    context = {
        'num_vehicle': num_vehicle,
        'num_action': num_action,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.order_by('rok_produkcji')
    return render(request, 'vehicle_lista.html', {'vehicles': vehicles})

@login_required
def action_list(request):
    actions = Action.objects.order_by('data_wykonania').reverse()
    suma_kosztow = 0
    for kwotka in (actions.values_list('koszt')):
        suma_kosztow = suma_kosztow + kwotka[0]
    #Action.objects.aggregate(sum('koszt'))
    context = {
        'suma_kosztow': suma_kosztow,
        'actions': actions
    }
    return render(request, 'action_lista.html', context = context)

@login_required
def action_list_vehicle(request, id_vehicle):
    actions = Action.objects.filter(vehicle=id_vehicle).order_by('data_wykonania').reverse()
    suma_kosztow = 0
    for kwotka in (actions.values_list('koszt')):
        suma_kosztow = suma_kosztow + kwotka[0]
    context = {
            'suma_kosztow': suma_kosztow,
            'actions': actions
            }

    return render(request, 'action_lista.html', context = context)


class ActionCreate(LoginRequiredMixin, CreateView ):
	model = Action
	form_class = ActionCreateForm

	'''
	def form_valid(self, form):
		form.instance.manager = self.request.user
		#print(self.kwargs)
		klub = Klub.objects.filter(id = self.kwargs['klubzawodnika'])[0]
		form.instance.klub = klub
		return super().form_valid(form)
	'''

	#fields='__all__'


	#fields = ['first_name', 'name', 'sex','full_birth', 'year_of_birth', 'weight', 'klub', 'PESEL']
	#initial = {'date_of_death': '11/06/2020'}
	#success_url = reverse_lazy('zawodnik/'+str(Zawodnik.id))

class ActionDetailView(LoginRequiredMixin, generic.DetailView):
	model = Action

class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
	model = Vehicle

class VehicleSubmit(LoginRequiredMixin, UpdateView ):
	model = Vehicle
	form_class = VehicleSubmitForm
