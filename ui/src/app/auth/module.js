(function(angular){
    "use strict";
    angular.module("2factor.auth", [
        "2factor.common.services",
        "2factor.auth.services",
        "2factor.auth.interceptors",
        "2factor.auth.forms",
        "2factor.auth.controllers",
        "2factor.auth.routes"
    ]);

})(angular);
