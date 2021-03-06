(function(angular){
    "use strict";
    angular.module("2factor.auth.interceptors", ["2factor.common.services"])

    .service("2Factor.Auth.AuthInterceptor", ["$window", "storageService","AUTH_KEY",
        function($window, storage, AUTH_KEY){
        return {
            request: function(config){
                config.headers = config.headers || {};
                if(storage.retrieve(AUTH_KEY)){
                    var token = storage.retrieve(AUTH_KEY).token;
                    config.headers.Authorization = "Token " + token;
                }
                return config;
            },
            response: function(response){
                if (response.status === 401) {
                    storage.remove(AUTH_KEY);
                    $window.location.replace("/login");
                }
                return response || $q.when(response);
            }
        };

    }]);

})(angular);
