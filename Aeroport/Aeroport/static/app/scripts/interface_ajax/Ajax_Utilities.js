/**
    This file containes a class who helps you to use AJAX with jQuery
**/

class Ajax {
    /**
     * @param {string} url -> endpoint
     * @param {object} data -> data
     */
    constructor(url,data) {
        this.url = url;
        this.data = data;
        this.csrf_token = Cookies.Get('csrftoken');
        console.log(this.csrf_token);
    }

    /**
     * Call Ajax method with verb action
     * @param {string} verb
     * @returns {object} data -> data if success 
     */
    AjaxCall(verb) {
        $.ajaxSetup({
            headers: { "X-CSRFToken": this.csrf_token }
        });
        let response;

        $.ajax({
            url: this.url,
            method: verb,
            data: JSON.stringify(this.data),
            cache: false,
            contentType: "application/json"
        }).then(data => { response = data; });
        return data;
    }

    /**
     * Call Ajax method with get action
     */
    Get() {
        return this.AjaxCall('GET');
    }

    /**
     * Call Ajax method with post action
     */
    Post() {
        return this.AjaxCall('POST');
    }

    /**
     * Call Ajax method with put action
     */
    Put() {
        return this.AjaxCall('PUT');
    }

    /**
     * Call Ajax method with post action
     */
    Delete() {
        return this.AjaxCall('DELETE');
    }
}