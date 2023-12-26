from django.shortcuts import render
from django.contrib import messages

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
        selected_date_text = request.GET['selectedDateText']

        try:
            #Try to retrieve the DateTimeTravel object for the selected date.
            selected_date = datetime.strptime(selected_date_text, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_time_travel = DateTimeTravel.objects.get(date=selected_date)

            #Now, you can retrieve the TravelBoard object associated with this DateTimeTravel.
            travel_board = date_time_travel.travel.travelboard

            #Combine the selected date with the current time for comparison.
            #selected_datetime = datetime.combine(date_time_travel.date, travel_board.time_board)
            #if selected_datetime < datetime.now(): I will check it after

            response_data = {
                'board': travel_board.board,
            }

            return JsonResponse(response_data)
        
        except DateTimeTravel.DoesNotExist:
            return JsonResponse({'error': 'No matching DateTimeTravel found for the selected date'})
        
    else:
        return JsonResponse({'error': 'Invalid request'})