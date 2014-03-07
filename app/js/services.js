'use strict';

/* Services */

var fqServices = angular.module('fqServices', ['ngResource']);

fqServices.factory('ImageService', ['$resource',
    function($resource){
        return $resource('data/images/:imageName', {}, {
            query: {method:'GET', params:{imageName:''}, isArray:true}
        });
    }]);


fqServices.factory('FeatureLookupService', ['$resource',
    function($resource){
        return $resource('data/featureLookup.json', {}, {
            query: {method:'GET', params:{}, isArray:true}
        });
    }]);


