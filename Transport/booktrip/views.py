from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import TravelBoard
from .models import TravelDestination
from .models import Travel
from .models import LocalBoard
from .models import LocalDestination
from .models import DateTimeTravel

def index(request):



    #yearDate = datetime.now().year
    #monthDate = datetime.now().month
    #dayDate = datetime.now().day
    
    #cal = HTMLCalendar().formatmonth(yearDate, monthDate, dayDate)

    #dateTimeTravel = DateTimeTravel.objects.filter(date__gte=datetime.now().date()).order_by('-date')
    #print(dateTimeTravel.values_list('date', flat=True))

    #print(datetime.now().date())
    #print(DateTimeTravel.objects.first().date)
    #print(dateTimeTravel)

    #context = {
    #    'dateTimeTravel': dateTimeTravel
    #}

    #return render(request, 'booktrip/booktrip.html', context)   , {'cal' : cal}
    return render(request, 'booktrip/booktrip.html')

