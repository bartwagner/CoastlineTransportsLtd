from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

from .models import DateTimeTravel
#from .models import TravelBoard
#from .models import TravelDestination
#from .models import Travel
#from .models import LocalBoard
#from .models import LocalDestination


def index(request):
    #Retrieve all instances of DateTimeTravel with dates greater than or equal to the current date.
    date_time_travel_avaliable = DateTimeTravel.objects.filter(date__gte=datetime.today())
    
    #Create a dictionary with the available dates and the associated price for each one.
    date_avaliable = [event.date.strftime('%Y-%m-%d') for event in date_time_travel_avaliable]

    return render(request, 'booktrip/booktrip.html', {'date_avaliable': date_avaliable })

def handle_selected_date(request):
    if request.method == 'GET' and 'selectedDateText' in request.GET:
        selected_date = request.GET['selectedDateText']
        response_data = {'selected_date': selected_date}

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request'})