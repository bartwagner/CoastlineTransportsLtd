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
                url: 'handle-selected-date/',
                data: {'selectedDateText': selectedDateText},
                dataType: 'json',
                success: function(response) {
                    $('#selectBoard').html(`<option value="${response.board}" selected>${response.board}</option>`);
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