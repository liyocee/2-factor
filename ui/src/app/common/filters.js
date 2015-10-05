(function(angular){
    "use strict";
    angular.module("2factor.common.filters", [])
    .filter("dateFilter", [function(){
        return function(input){
            return moment(input).format("MMM Do, YYYY");
        };
    }]);
})(angular);
