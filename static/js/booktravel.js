function initializeDatePicker(datesAvailable) {
    function enableDays(date) {
        var dateString = $.datepicker.formatDate("yy-mm-dd", date);
        var isDateAvailable = datesAvailable.indexOf(dateString) !== -1;
        return [isDateAvailable, dateString];
    }
    $("#eventDate").datepicker({
        beforeShowDay: enableDays,
        onSelect: function(selectedDateText) {
            $.ajax({
                url: 'handle-selected-date-board/',
                data: {'selectedDateText': selectedDateText},
                dataType: 'html',
                success: function(response) {
                    $('#selectBoard').html(response);
                    $('#selectDestination').html('<option value="" selected>Select the board first.</option>');
                },
                error: function(error) {
                    console.error('AJAX Error:', error);
                }
            });
        }
    });
}
$(document).ready(function() {
    initializeDatePicker(datesAvailable);
});

function handleBoardSelection() {
    var selectedBoard = $('#selectBoard').val();
    var selectedDateText = $('#eventDate').val();

    if (selectedBoard) {
        $.ajax({
            url: 'handle-selected-board-destination/',
            data: {'selectedBoard': selectedBoard, 'selectedDateText': selectedDateText},
            dataType: 'html',
            success: function(response) {
                $('#selectDestination').html(response);
            },
            error: function(error) {
                console.error('AJAX Error:', error);
            }
        });
    } else {
        //Clean options if anyone board was selected
        $('#selectDestination').html('<option value="" selected>Select the board first.</option>');
        $('#selectLocalBoard').html('<option value="" selected>Select the destination first.</option>');
        $('#selectLocalDestination').html('<option value="" selected>Select the destination first.</option>');
    }
}

function handleDestinationSelection(){
    var selectedBoard = $('#selectBoard').val();
    var selectedDateText = $('#eventDate').val();
    var selectDestination = $('#selectDestination').val();

    if (selectDestination) {
        $.ajax({
            url: 'handle-selected-local-board-destination/',
            data: {'selectDestination': selectDestination, 'selectedBoard': selectedBoard, 'selectedDateText': selectedDateText},
            dataType: 'json',
            success: function(response) {
                $('#selectLocalBoard').html(response.local_boards.join(''));
                $('#selectLocalDestination').html(response.local_destinations.join(''));
            },
            error: function(error) {
                console.error('AJAX Error:', error);
            }
        });
    } else {
        //Clean options if anyone board was selected
        $('#selectLocalBoard').html('<option value="" selected>Select the destination first.</option>');
        $('#selectLocalDestination').html('<option value="" selected>Select the destination first.</option>');
    }
}