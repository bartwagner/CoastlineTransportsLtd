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
    }
}