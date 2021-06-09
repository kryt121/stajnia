from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),

	path('vehicle_lista.html', views.vehicle_list, name='vehicle_lista'),
	path('action_lista.html', views.action_list, name='action_lista'),

    path('action/create/', views.ActionCreate.as_view(), name='action-create'),
    path('action/<int:pk>', views.ActionDetailView.as_view(), name='action-detail'),

    path('action_lista/<int:id_vehicle>', views.action_list_vehicle, name='action_lista_vehicle'),

    path('vehicle/submit/<int:pk>', views.VehicleSubmit.as_view(), name='vehicle-submit'),
    path('vehicle/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle-detail'),
	]
