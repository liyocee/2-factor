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
        ["$scope","$stateParams", "2Factor.Auth.AuthService", "2Factor.Form.Login",
        function ($scope,$stateParams, AuthService, Form) {
            var vm = this;
            vm.user = {};
            vm.userFields = Form.getForm();
            vm.login = function(user){
                AuthService.login(
                    user.username, user.password, $scope);
            };
        }]
    )
    .controller("2Factor.VerifyEmail.Controller",
        ["$scope","$stateParams", "2Factor.Auth.AuthService",
        function ($scope,$stateParams, AuthService) {
            AuthService.verifyEmail($stateParams.token, $stateParams.id, $scope);
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
                        $state.go("login");
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
