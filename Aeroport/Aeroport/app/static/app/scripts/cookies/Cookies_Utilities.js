/**
    This file contain an API class for cookies 
**/

class Cookies {
    /**
     * @param {string} cname
     */
    static Get(cname) {
        let cookiesString = decodeURIComponent(document.cookie);
        for (const cookie of cookiesString.split(";")) {
            if (cookie.match(cname) != null) {
                return cookie.split("=")[1];
            }
        }
        return "undefined";
    }
}