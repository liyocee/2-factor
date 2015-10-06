(function(angular){
    angular.module("2factor.auth.forms.registration", ["2factor.common"])

    .service("2Factor.Member.Form.Registration", function(){
        var registrationFormFields = function(options){
            return [
                {
                    key: "first_name",
                    type: "input",
                    templateOptions: {
                        placeholder: "First Name",
                        label: "First Name:",
                        type: "text",
                        required:true
                    }
                },
                {
                    key: "last_name",
                    type: "input",
                    templateOptions: {
                        placeholder: "Last Name",
                        label: "Last Name:",
                        type: "text",
                        required:true
                    }
                },
                {
                    key: "email",
                    type: "input",
                    templateOptions: {
                        placeholder: "Email",
                        type: "email",
                        label: "Email:",
                        required:true
                    }

                },
                {
                    key: "phone_number",
                    type: "input",
                    templateOptions: {
                        placeholder: "Phone Number",
                        type: "text",
                        label: "Phone Number:",
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
                    key: "confirmPassword",
                    optionsTypes: ["matchField"],
                    model: options.password.model,
                    type: "input",
                    templateOptions: {
                        "type": "password",
                        "label": "Confirm Password",
                        "placeholder": "Please re-enter your password",
                        "required": true
                    },
                    data: {
                        "fieldToMatch": "password",
                        "modelToMatch": options.user.model,
                        "matchFieldMessage": "$viewValue + \" does not match \" + options.data.modelToMatch.email"
                    }
                },
                {
                    key: "terms_of_use",
                    type: "checkbox",
                    templateOptions: {
                        label: "I Agree to Terms of use.",
                        required:true
                    }

                }
            ];
        };
        this.getForm = function(options){
            return registrationFormFields(options);
        };

    });
})(angular);
