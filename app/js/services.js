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

fqServices.factory('FeatureQueryService', ['$resource', '$http',
    function( $resource){
        return $resource('http://localhost\\:8080/login',null , {
            'update': { method:'POST', data : {} }
        });
    }]);

