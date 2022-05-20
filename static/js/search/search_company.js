$(document).ready(function () {
    load_data_item();
    function load_data_item(query = '') {
        $.ajax({
            url: "/companyrecords",
            method: "POST",
            data: { query: query },
            success: function (data) {
                $('tbody').html(data);
                $('tbody').append(data.htmlresponse);
            }
        })
    }

    $('#search_filter').change(function () {
        $('#hidden_value').val($('#search_filter').val());
        var query = $('#hidden_value').val();
        load_data_item(query);
    });

});