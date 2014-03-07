'use strict';

/* App Module */

var featureQueryApp = angular.module('featureQueryApp', [
    'ngRoute',
   'featureQueryControllers', 'fqServices'


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
            otherwise({
                redirectTo: '/locations'
            });
    }]);
