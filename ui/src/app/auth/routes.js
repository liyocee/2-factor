(function(anglular){
    "use strict";
    angular.module("2factor.auth.routes", [
        "2factor.auth.controllers"
    ])
    .config(function config($stateProvider) {
        $stateProvider
            .state("login", {
                url: "/login",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/login.tpl.html",
                        controller: "2Factor.Login.Controller as vm"
                    },
                    "header@login": {
                        templateUrl: "common/tpls/sub_header.tpl.html"
                    },
                    "error@login": {
                        templateUrl: "common/tpls/error.tpl.html"
                    }
                },
                data: {pageTitle: "Member Login"}
            })
            .state("signup", {
                url: "/signup",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/signup.tpl.html",
                        controller: "2Factor.MemberRegistration.Controller as vm"
                    },
                    "header@signup": {
                        templateUrl: "common/tpls/sub_header.tpl.html"
                    }
                },
                data: {pageTitle: "Member Signup"}
            });
    });

})(angular);
