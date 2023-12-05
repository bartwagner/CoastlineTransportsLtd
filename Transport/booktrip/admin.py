from django.contrib import admin

from .models import Vehicle
from .models import Travel
from .models import LocalBoard
from .models import LocalDestination
from .models import DateTimeTravel

#admin.site.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number', 'sets')
    list_filter  = ('number', 'sets')
admin.site.register(Vehicle, VehicleAdmin)

#admin.site.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'board', 'time_board', 'destination', 'time_destination')
    list_filter  = ('vehicle', 'board', 'time_board', 'destination', 'time_destination')
admin.site.register(Travel, TravelAdmin)

#admin.site.register(LocalDestination)
class LocalDestinationAdmin(admin.ModelAdmin):
    list_display = ('travel', 'local_destination', 'time_destination')
    list_filter  = ('travel', 'local_destination', 'time_destination')
admin.site.register(LocalDestination, LocalDestinationAdmin)

#admin.site.register(LocalBoard)
class LocalBoardAdmin(admin.ModelAdmin):
    list_display = ('travel', 'local_board', 'time_board')
    list_filter  = ('travel', 'local_board', 'time_board')
admin.site.register(LocalBoard, LocalBoardAdmin)


#admin.site.register(DateTimeTravel)
class DateTimeTravelAdmin(admin.ModelAdmin):
    list_display = ('travel', 'date', 'price')
    list_filter  = ('travel', 'date', 'price')
admin.site.register(DateTimeTravel, DateTimeTravelAdmin)