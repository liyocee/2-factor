(function (window) {
    "use strict";
    // Resolve conflict in jQuery UI tooltip with Bootstrap tooltip
    var setts = {
        "SERVER_URL": "http://localhost:8000/api/v1",
        "DEBUG": true,
        "ACTIONS": {
            "RESTRICT": []
        }
    };

    window.TWO_FACTOR_SETTINGS = setts;

})(window);
