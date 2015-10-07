(function(angular){
    "use strict";
    angular.module("2factor.auth.services", ["2factor.common.services"])
    .service("2Factor.Auth.AuthService", ["$state","$window", "$http", "Restangular", "storageService",
        "HOME_PAGE_NAME","AUTH_KEY", "2Factor.Notification",
        function($state,$window, $http, api, storage, HOME_PAGE, AUTH_KEY, notification){
        var storeKey = AUTH_KEY;
        var setCredentials = function(credz){
            storage.store(storeKey, credz);
        };

        var getToken = function(){
            var credz = storage.retrieve(storeKey);
            if(credz){
                return credz.token;
            }
        };

        var getUser = function(){
            var credz = storage.retrieve(storeKey);
            if(credz){
                return credz.user;
            }else{
                $state.go("login");
            }
        };

        var login = function(username, password, scope){
            var data = {
                username: username,
                password: password
            };
            scope.login_promise = api.all("auth").all("login").post(data);
            scope.login_promise.then(
                function(data){
                    if(!data.user.is_email_verified){
                        scope.alert = "Click on the verification link sent to you.";
                        notification.error("Error", "Error logging in");
                        return;
                    }
                    var credz = {
                        token: data.key,
                        user: data.user
                    };
                    setCredentials(credz);
                    // $window.location.replace("/dashboard");
                    $state.go("token");
                    notification.success("Login", "Successfully logged in");
                },
                function(error){
                    scope.alert = "Invalid username/password combination";
                    notification.error("Error", "Error logging in");
                });
        };

        var smsToken = function(token, scope){
            console.log(token);
            scope.alert = "Invalid Token";
        };

        var verifyEmail = function(token, userId, scope){
            console.log(userId);
            scope.alert = token + "Verified";
        };
        var logout = function(){
            storage.remove(storeKey);
            api.all("auth").all("logout").post({}).then(
                function(data){
                    $state.go("home");
                },
                function(error){
                    $state.go("home");
                });

        };

        var register = function(data){
            var baseApi = api.all("user");
            return baseApi.all("create").post(data);
        };

        return {
            "setCredentials": setCredentials,
            "getToken": getToken,
            "login": login,
            "logout": logout,
            "getUser": getUser,
            "register": register,
            "smsToken": smsToken,
            "verifyEmail": verifyEmail
        };
    }])
    ;
})(angular);
