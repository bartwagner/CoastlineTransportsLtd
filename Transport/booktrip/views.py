from django.shortcuts import render
from datetime import datetime
from .models import Travel

#from .models import DateTimeTravel

def index(request):
    travel = Travel.objects.first()

    print(travel)

    #dateTimeTravel = DateTimeTravel.objects.filter(date__gte=datetime.now().date()).order_by('-date')

    #print(datetime.now().date())
    #print(DateTimeTravel.objects.first().date)
    #print(dateTimeTravel)

    #context = {
    #    'dateTimeTravel': dateTimeTravel
    #}

    #return render(request, 'booktrip/booktrip.html', context)
    return render(request, 'booktrip/booktrip.html')

