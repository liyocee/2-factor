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
            .state("verify_email", {
                url: "/verify_email/:token/:id",
                views: {
                    "main-container": {
                        controller: "2Factor.VerifyEmail.Controller as vm",
                        templateUrl: "auth/tpls/verify_email.tpl.html"
                    },
                    "error@verify_email": {
                        templateUrl: "common/tpls/error.tpl.html"
                    }
                },
                data: {pageTitle: "Member Login"}
            })
            .state("token", {
                url: "/token/:user",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/token.tpl.html",
                        controller: "2Factor.Token.Controller as vm"
                    },
                    "error@token": {
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
            })
            .state("signup_msg", {
                url: "/message",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/signup_msg.tpl.html"
                    }
                },
                data: {pageTitle: "Member Signup"}
            });
    });

})(angular);
