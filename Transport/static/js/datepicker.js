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
                    // Atualize o valor do parágrafo com o valor recebido
                    $('#selectedDateParagraph').text('selected: ' + response.selected_date);
                },
                error: function(error) {
                    console.error('Erro na solicitação AJAX:', error);
                }
            });
        }
    });
}
$(document).ready(function() {
    initializeDatePicker(datesAvailable);
});