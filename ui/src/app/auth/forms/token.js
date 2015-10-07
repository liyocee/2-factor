(function(angular){
    angular.module("2factor.auth.forms.token", ["2factor.common.utils.forms"])

    .service("2Factor.Form.Token", function(){
        var formFields = function(options){
            return [
                {
                    key: "token",
                    type: "input",

                    templateOptions: {
                        placeholder: "Token",
                        label: "SMS Code:",
                        type: "number",
                        required:true
                    }

                }
            ];
        };
        this.getForm = function(options){
            return formFields(options);
        };

    });
})(angular);
