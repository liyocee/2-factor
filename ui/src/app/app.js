(function(angular){
    "use strict";
    angular.module("2factorApp", [
        //third-party stuff
        "ngAnimate",
        "ngCookies",
        "formly",
        "formlyBootstrap",
        "xeditable",
        "ui.select",
        "restangular",
        "cgBusy",
        "ngTable",
        //our stuff
        "templates-app",
        "2factorConfig",
        "2factor.home",
        "2factor.dashboard",
        "2factor.common",
        "2factor.auth"
    ])
    .run(["editableOptions", function(editableOptions){
        editableOptions.theme = "bs3";
    }]);

})(angular);
