'use strict';

/* App Module */

var featureQueryApp = angular.module('featureQueryApp', [
    'ngRoute',
   'featureQueryControllers', 'fqServices','featureQueryDirectives', 'featureQueryFilters'
]);

featureQueryApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/locations', {
                templateUrl: 'partials/locations.html'
            }).
            when('/jlocations', {
                templateUrl: 'partials/jlocations.html'
            }).
            when('/image/:imageName', {
                templateUrl: 'partials/image.html'
            }).
            when('/jimage/:imageName', {
                templateUrl: 'partials/jimage.html'
            }).
			when('/syslog', {
                templateUrl: 'partials/syslog.html'
            }).
			when('/querylog', {
                templateUrl: 'partials/querylog.html'
            }).
			when('/testlog', {
                templateUrl: 'partials/unittestlog.html'
            }).
            otherwise({
                redirectTo: '/locations'
            });
    }]);


