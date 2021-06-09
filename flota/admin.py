from django.contrib import admin

from .models import Vehicle, Action

class VehicleAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'nr_rej', 'typ_pojazdu', 'uwagi','rok_produkcji','przebieg', 'przeglad_techniczny', 'ubezpieczenie', 'wymiana_oleju'  )
	#list_filter = ('klub', 'sex')
	fields=( 'typ_pojazdu',('nazwa', 'nr_rej'),('rok_produkcji','przebieg'), 'uwagi', 'przeglad_techniczny', 'ubezpieczenie', 'wymiana_oleju')

class ActionAdmin(admin.ModelAdmin):
	list_display = ('vehicle', 'data_wykonania', 'nazwa', 'koszt', 'przebieg','uwagi')
	list_filter = ('vehicle', 'nazwa')
	fields=( 'vehicle',('nazwa', 'koszt'),('data_wykonania', 'przebieg'), 'uwagi')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Action, ActionAdmin)




