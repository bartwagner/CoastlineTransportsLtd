function initializeDatePicker(datesAvailable) {
    function enableDays(date) {
        var dateString = $.datepicker.formatDate("yy-mm-dd", date);
        var isDateAvailable = datesAvailable.indexOf(dateString) !== -1;
        return [isDateAvailable, dateString];
    }
  
    $("#eventDate").datepicker({
        beforeShowDay: enableDays,
        onSelect: function(selectedDateText) {
            alert('You selected the date: ' + selectedDateText);
        }
    });
}
  
$(document).ready(function() {
    initializeDatePicker(datesAvailable);
});