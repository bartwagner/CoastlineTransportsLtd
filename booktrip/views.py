from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import DateTimeTravel

def index(request):
    #Retrieve all instances of DateTimeTravel with dates greater than or equal to the current date.
    date_time_travel_avaliable = DateTimeTravel.objects.filter(date__gte=datetime.today())
    
    #Create a list of available dates, considering date and time conditions.
    date_avaliable = []
    for event in date_time_travel_avaliable:
        selected_datetime = datetime.combine(event.date, event.travel.travelboard.time_board)
        if selected_datetime > datetime.now():
            date_avaliable.append(event.date.strftime('%Y-%m-%d'))

    return render(request, 'booktrip/booktrip.html', {'date_avaliable': date_avaliable })

def handle_selected_date_board(request):
    if request.method == 'GET' and 'selectedDateText' in request.GET:
        selected_date_text = request.GET['selectedDateText']

        try:
            #Try to retrieve the DateTimeTravel object for the selected date.
            selected_date = datetime.strptime(selected_date_text, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_time_travel = DateTimeTravel.objects.get(date=selected_date)

            #Now, you can retrieve the TravelBoard object associated with this DateTimeTravel and send to display board and time board.
            travel_board = date_time_travel.travel.travelboard
            board = travel_board.board + ' - ' + str(travel_board.time_board)

            option_html = '<option value="" selected>Select the options below.</option>'
            option_html += f'<option value="{board}">{board}</option>'

            return HttpResponse(option_html)
        
        except DateTimeTravel.DoesNotExist:
            return HttpResponse('<option value="">No matching travel found for the selected date</option>')
        
    else:
        return HttpResponse('<option value="" selected>Invalid request</option>')

def handle_selected_board_destination(request):
    if request.method == 'GET' and 'selectedBoard' in request.GET and 'selectedDateText' in request.GET:
        selected_board = request.GET['selectedBoard']
        selected_date_text = request.GET['selectedDateText']

        try:

            print(selected_date_text)
            print(selected_board)

            option_html = '<option value="" selected>Select the options below.</option>'

            return HttpResponse(option_html)
        except DateTimeTravel.DoesNotExist:
            return HttpResponse('<option value="">No matching travel found for the selected date</option>')
    else:
        return HttpResponse('<option value="" selected>Invalid request</option>')