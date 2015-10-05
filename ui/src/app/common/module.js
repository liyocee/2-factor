(function(angular){
    "use strict";
    angular.module("2factor.common", [
        "ui.router",
        "2factor.common.routes",
        "2factor.common.utils",
        "2factor.common.filters",
        "2factor.common.services",
        "2factor.common.directives"
    ]);

})(angular);
