$(document).ready(function () {
    $('#make-short').on('submit', function (event) {
        event.preventDefault();
        console.log('click');
        $.post('/add/', { primary : $('#long_url').val()}, function (data) {
            console.log(data);
            $('#long_url').val('');
            $('.result__url').text(data.shorten);
        })
    })
});