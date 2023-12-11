from django.contrib import admin

from .models import Vehicle
from .models import TravelBoard
from .models import TravelDestination
from .models import Travel
from .models import LocalDestination
from .models import LocalBoard
from .models import DateTimeTravel

#admin.site.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number', 'sets')
    list_filter  = ('number', 'sets')
    search_fields = ('number', 'sets')
    list_per_page = 25
admin.site.register(Vehicle, VehicleAdmin)

#admin.site.register(TravelBoardAdmin)
class TravelBoardAdmin(admin.ModelAdmin):
    list_display = ('board', 'time_board')
    list_filter  = ('board', 'time_board')
    search_fields = ('board', 'time_board')
    list_per_page = 25
admin.site.register(TravelBoard, TravelBoardAdmin)

#admin.site.register(TravelDestination)
class TravelDestinationAdmin(admin.ModelAdmin):
    list_display = ('destination', 'time_destination')
    list_filter  = ('destination', 'time_destination')
    search_fields = ('destination', 'time_destination')
    list_per_page = 25
admin.site.register(TravelDestination, TravelDestinationAdmin)

#admin.site.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'travelboard', 'traveldestination')
    list_filter  = ('vehicle', 'travelboard', 'traveldestination')
    search_fields = ('travelboard','traveldestination')
    list_per_page = 25
admin.site.register(Travel, TravelAdmin)

#admin.site.register(LocalDestination)
class LocalDestinationAdmin(admin.ModelAdmin):
    list_display = ('travel', 'local_destination', 'time_destination')
    list_filter  = ('travel', 'local_destination', 'time_destination')
    search_fields = ('local_destination', 'time_destination')
    list_per_page = 25
admin.site.register(LocalDestination, LocalDestinationAdmin)

#admin.site.register(LocalBoard)
class LocalBoardAdmin(admin.ModelAdmin):
    list_display = ('travel', 'local_board', 'time_board')
    list_filter  = ('travel', 'local_board', 'time_board')
    search_fields = ('local_board', 'time_board')
    list_per_page = 25
admin.site.register(LocalBoard, LocalBoardAdmin)

#admin.site.register(DateTimeTravel)
class DateTimeTravelAdmin(admin.ModelAdmin):
    list_display = ('travel', 'date', 'price')
    list_filter  = ('travel', 'date', 'price')
    search_fields = ('date', 'price')
    list_per_page = 25
admin.site.register(DateTimeTravel, DateTimeTravelAdmin)