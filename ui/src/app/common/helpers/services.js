(function(angular){
    "use strict";
    angular.module("2factor.common.utils.services", [])
    .service("2Factor.HelperService", ["School.Auth.AuthService", function(AuthService){
        return {
            addSchool: function(data){
                var school = {school: AuthService.getUser().school.id};
                return _.extend(data, school);
            }
        };
    }]);
})(angular);
