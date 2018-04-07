/**
    This file contains all forms submission
**/

/* find_flights form */
$("#module_flights > .content > form").submit(function (event) {
    event.preventDefault();
    let dataSend = {
        departure_id: $('select[name="depart"] > option:selected').val(),
        arrival_id: $('select[name="arrivee"] > option:selected').val()
    };

    let response = new Ajax(this.action, dataSend).Post();
    response.then(data => console.log(data));
});