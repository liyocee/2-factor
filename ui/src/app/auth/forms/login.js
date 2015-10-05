(function(angular){
    angular.module("2factor.auth.forms.login", ["2factor.common.utils.forms"])

    .service("2Factor.Form.Login", function(){
        var formFields = function(options){
            return [
                {
                    key: "username",
                    type: "input",

                    templateOptions: {
                        placeholder: "Username",
                        label: "Username:",
                        required:true
                    }

                },
                {
                    key: "password",
                    type: "input",
                    templateOptions: {
                        placeholder: "Password",
                        type: "password",
                        label: "Password:",
                        required:true
                    }

                },
                {
                    key: "keepMeLogged",
                    type: "checkbox",
                    templateOptions: {
                        label: "Keep me logged in",
                        required:false
                    }

                }
            ];
        };
        this.getForm = function(options){
            return formFields(options);
        };

    });
})(angular);
