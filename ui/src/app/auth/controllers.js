(function(angular){
    "use strict";
    angular.module("2factor.auth.controllers", [
        "2factor.auth.services",
        "2factor.auth.forms",
        "2factor.common.services"
    ])
    .controller("2Factor.UserProfile.Controller",
        ["2Factor.Auth.AuthService", "2Factor.Notification",
        function (AuthService, notification) {
            var vm = this;
            vm.user = AuthService.getUser();
            vm.logout = function(){
                notification.info("Logout", "Successfully logged out");
                AuthService.logout();
            };
        }]
    )

    .controller("2Factor.Login.Controller",
        ["storageService","$scope","$stateParams", "2Factor.Auth.AuthService", "2Factor.Form.Login",
        "2Factor.Notification", "verifyEmail",
        function (storage,$scope,$stateParams, AuthService, Form, notification, verifyEmail) {
            var vm = this;
            vm.user = {};
            vm.userFields = Form.getForm();
            if(verifyEmail.id && verifyEmail.token){
                var data = verifyEmail;
                vm.promise = AuthService.verifyEmail(data.token, data.id, $scope);
                vm.promise.then(function(data){
                    // $state.go("login");
                }, function(error){
                    $scope.alert = "Your email couldn't be verified";
                    notification.error("Error", "Verification Failed");
                    console.log(error);
                });
            }
            vm.login = function(user){
                AuthService.login(
                    user.username, user.password, $scope);

            };
        }]
    )
    .controller("2Factor.VerifyEmail.Controller",
        ["$scope","$timeout", "2Factor.Auth.AuthService", "$state",
        "2Factor.Notification", "verifyEmail",
        function ($scope,$timeout, AuthService, $state, notification, verifyEmail) {
            var vm = this;
            var data = verifyEmail;
            $timeout(function(){
                vm.promise = AuthService.verifyEmail(data.token, data.id, $scope);
                vm.promise.then(function(data){
                    $state.go("login");
                }, function(error){
                    $scope.alert = "Your email couldn't be verified";
                    notification.error("Error", "Verification Failed");
                    console.log(error);
                });
            }, 5000);

        }]
    )
    .controller("2Factor.Token.Controller",
        ["$scope","$stateParams", "2Factor.Auth.AuthService", "2Factor.Form.Token",
        function ($scope,$stateParams, AuthService, Form) {
            var vm = this;
            vm.token = {};
            vm.tokenFields = Form.getForm();
            vm.smsToken = function(token){
                AuthService.smsToken(
                    token, $stateParams.user, $scope);
            };
        }]
    )
    .controller("2Factor.MemberRegistration.Controller",
        ["$scope","$state", "2Factor.Member.Form.Registration",
        "2Factor.Auth.AuthService", "2Factor.Notification",
        "storageService","AUTH_KEY",
        function ($scope, $state, Form, AuthService, notification, storage, AUTH_KEY) {
            storage.remove(AUTH_KEY);
            var vm = this;
            vm.user = {
                first_name: "",
                last_name: "",
                email: "",
                password: ""
            };
            vm.confirmPassword = {};
            var formOptions = {
                user: {model: vm.user},
                password: {model: vm.confirmPassword}
            };
            vm.userFields = Form.getForm(formOptions);
            vm.signup = function(user){
                vm.promise = AuthService.register(user);
                vm.promise.then(
                    function(){
                        notification.success("Success", "Registration was successful");
                        $state.go("signup_msg");
                    },
                    function(error){
                        notification.error("Error", "An error occured");
                        console.log(error);
                    }
                );
            };
        }]
    )
    ;

})(angular);
