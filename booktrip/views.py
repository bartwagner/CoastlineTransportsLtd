from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import DateTimeTravel, LocalBoard, LocalDestination
from django.http import JsonResponse

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
            date_time_travels = DateTimeTravel.objects.filter(date=selected_date)

            #Initialize the option_html with the default option.
            option_html = '<option value="" selected>Select the options below.</option>'

            #Iterate over all DateTimeTravel instances for the selected date, date_board and and board to concatenate.
            for date_time_travel in date_time_travels:
                #Retrieve the TravelBoard object associated with each DateTimeTravel.
                travel_board = date_time_travel.travel.travelboard
                board = travel_board.board + ' - ' + str(travel_board.time_board)
                #Concatenate board and time_board and add it to the option_html.
                option_html += f'<option value="{board}">{board}</option>'

            return HttpResponse(option_html)
        
        except (DateTimeTravel.DoesNotExist, ValueError):
            return HttpResponse('<option value="">No matching travel found for the selected date</option>')
        
    else:
        return HttpResponse('<option value="" selected>Invalid request</option>')

def handle_selected_board_destination(request):
    if request.method == 'GET' and 'selectedBoard' in request.GET and 'selectedDateText' in request.GET:
        selected_board = request.GET['selectedBoard']
        selected_date_text = request.GET['selectedDateText']

        try:
            #Try to retrieve the DateTimeTravel object for the selected date, board and time_board.
            selected_date = datetime.strptime(selected_date_text, '%m/%d/%Y').strftime('%Y-%m-%d')
            board, time_board = selected_board.split(' - ')
            date_travel_destinations = DateTimeTravel.objects.filter(
                date=selected_date,
                travel__travelboard__board=board,
                travel__travelboard__time_board=time_board
            )

            #Initialize the option_html with the default option.
            option_html = '<option value="" selected>Select the options below.</option>'

            #Iterate over all DateTimeTravel instances for the selected date, date_destination and destination to concatenate.
            for date_travel_destination in date_travel_destinations:
                travel_destination = date_travel_destination.travel.traveldestination
                destination = travel_destination.destination + ' - ' + str(travel_destination.time_destination)
                option_html += f'<option value="{destination}">{destination}</option>'

            return HttpResponse(option_html)
        except (DateTimeTravel.DoesNotExist, ValueError):
            return HttpResponse('<option value="">No matching destinations found for the selected board and date</option>')
    else:
        return HttpResponse('<option value="" selected>Invalid request</option>')

def handle_selected_local_board_destination(request):
    if request.method == 'GET' and 'selectDestination' in request.GET and 'selectedBoard' in request.GET and 'selectedDateText' in request.GET:
        selected_destination = request.GET['selectDestination']
        selected_board = request.GET['selectedBoard']
        selected_date_text = request.GET['selectedDateText']
        
        try:
            #Try to retrieve the DateTimeTravel object for the selected date, board, time_board, destination and time_destination.
            selected_date = datetime.strptime(selected_date_text, '%m/%d/%Y').strftime('%Y-%m-%d')
            destination, time_destination = selected_destination.split(' - ')
            board, time_board = selected_board.split(' - ')
            date_travel_local_boards = LocalBoard.objects.filter(
                travel__travelboard__board=board,
                travel__travelboard__time_board=time_board,
                travel__traveldestination__destination=destination,
                travel__traveldestination__time_destination=time_destination                
            )
            date_travel_local_destinations = LocalDestination.objects.filter(
                travel__travelboard__board=board,
                travel__travelboard__time_board=time_board,
                travel__traveldestination__destination=destination,
                travel__traveldestination__time_destination=time_destination                
            )

            #Initialize the option_html with the default option.
            options_local_boards = ['<option value="" selected>Select the options below.</option>']
            options_local_destinations = ['<option value="" selected>Select the options below.</option>']


            #Iterate over all LocalBoard instances for the selected date, date_local_board, local_board to concatenate.
            for date_travel_local_board in date_travel_local_boards:
                localboard = date_travel_local_board.local_board + ' - ' + str(date_travel_local_board.time_board)
                options_local_boards.append(f'<option value="{localboard}">{localboard}</option>')
            
            #Iterate over all LocalDestination instances for the selected date, date_local_destination, local_destination to concatenate.
            for date_travel_local_destination in date_travel_local_destinations:
                localdestination = date_travel_local_destination.local_destination + ' - ' + str(date_travel_local_destination.time_destination)
                options_local_destinations.append(f'<option value="{localdestination}">{localdestination}</option>')

            return JsonResponse({'local_boards': options_local_boards, 'local_destinations': options_local_destinations})
        except (DateTimeTravel.DoesNotExist, ValueError):
            return HttpResponse('<option value="">No matching destinations found for the selected board and date</option>')
    else:
        return HttpResponse('<option value="" selected>Invalid request</option>')