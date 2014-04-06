'use strict';

/* App Module */

var featureQueryApp = angular.module('featureQueryApp', [
    'ngRoute',
   'featureQueryControllers', 'fqServices','featureQueryDirectives'


]);

featureQueryApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/locations', {
                templateUrl: 'partials/locations.html'
            }).
            when('/image/:imageName', {
                templateUrl: 'partials/image.html'
            }).
			when('/logs', {
                templateUrl: 'partials/logs.html'
            }).
            otherwise({
                redirectTo: '/locations'
            });
    }]);


