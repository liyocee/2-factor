(function(anglular){
    "use strict";

    angular.module("2factor.dashboard.routes", ["2factor.common"])

        .config(function config($stateProvider) {
            $stateProvider
                .state("base.dashboard", {
                    url: "/dashboard",
                    views: {
                        "content@base": {
                            templateUrl: "dashboard/tpls/dashboard.tpl.html"
                        }
                    },
                    data: {pageTitle: "Dashboard"},
                    options: {
                        reload: true
                    }
                });
        });

})(angular);
