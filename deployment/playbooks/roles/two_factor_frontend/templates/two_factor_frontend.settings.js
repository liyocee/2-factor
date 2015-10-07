(function (window) {
    "use strict";

    var setts = {
        "SERVER_URL": "{{server_url}}",
        "DEBUG": {{debug}},
        "ACTIONS": {
            "RESTRICT": []
        },
    };

    window.TWO_FACTOR_SETTINGS = setts;

})(window);
