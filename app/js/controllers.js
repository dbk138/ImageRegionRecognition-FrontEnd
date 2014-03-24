'use strict';
/* Controllers */

var featureQueryControllers = angular.module('featureQueryControllers', []);

featureQueryControllers.controller('LocationListCtrl', function($scope, LocationLookupService) {
   $scope.locations = LocationLookupService.query();
});

featureQueryControllers.controller('FeatureListCtrl', function($scope, $http) {
    $http.get('data/featureLookup.json').success(function(data) {
        $scope.features = data;
    });
});

featureQueryControllers.controller('CategoryListCtrl', function($scope, $http) {
    $http.get('data/featureLookup.json').success(function(data) {
        $scope.categories = data;
    });
});

featureQueryControllers.controller( 'testCtrl' , function ($scope, $http) {
    var words = [];
    $http.get('data/featureLookup.json').success(function(data) {
        for(var key in data) {
            words.push(key);
            //words.push(data[key].category);
        }
        words.sort();
    });
    $scope.tags = "";
    $scope.availableTags = words;
});

featureQueryControllers.controller('SubmitQuery', ['$scope','FeatureQueryService',function($scope, FeatureQueryService) {

    $scope.queryFeature = {};
    $scope.queryFeatureValue = {};
    $scope.submit = function() {

   var $ret = null;

       //$scope.queryFeature;
       //$scope.queryFeatureValue;
      //  FeatureQueryService.save()
        FeatureQueryService.update($scope.queryFeatureValue,$ret)
    }
}]);


featureQueryControllers.controller('ImageCtrl2', ['$scope','$http','$routeParams','ImageService','FeatureLookupService', 'LocationLookupService',
    function($scope, $http, $routeParams, ImageService,FeatureLookupService, LocationLookupService) {

        $scope.imageName = $routeParams.imageName;

        $scope.locations = LocationLookupService.query();
        

         ImageService.get({imageName:$scope.imageName.replace('/','_').concat('.json')}
            ,  //success function
            function (imgData) {

                var max = [];

                var summaryInfo ={};
                summaryInfo['URBAN/DEVELOPED']=imgData['data']['L1_100'];
                summaryInfo['AGRICULTURE']= imgData['data']['L1_110'];
                summaryInfo['GRASSLAND']=imgData['data']['L1_150'];
                summaryInfo['FOREST']=imgData['data']['L1_160'];
                summaryInfo['OPEN WATER']=imgData['data']['L1_200'];
                summaryInfo['WETLAND ']=imgData['data']['L1_210'];
                summaryInfo['BARREN']=imgData['data']['L1_240'];
                summaryInfo['SHRUBLAND']=imgData['data']['L1_250'];
                summaryInfo['CLOUD COVER']=imgData['data']['L1_255'];
                $scope.summaryInfo = summaryInfo;

                for( var index in summaryInfo) {
                    max.push(summaryInfo[index]);
                }

                var element = "";
                var value = "";
                var maxValue = Math.max.apply(this, max);

                for( var key in summaryInfo) {
                    if(summaryInfo[key] === maxValue.toString()) {
                        element = key;
                        value = (parseFloat(summaryInfo[key]) * 100).toFixed(2);
                    }
                }

                $scope.classification = element;
                $scope.elementValue = value;

                // lets get the feature lookup data here.
                //  notice i'm still inside the success function of the first service call.
                // Instead this functionality of marshalling the async calls should be done via promises.
                // but i don't know heck about promises as yet.

                FeatureLookupService.get({},
                // success function
                function(featureLookup) {
                    var queryBuilder = {};
                    for ( var feature in (imgData['data'])) {
                        if (imgData['data'].hasOwnProperty(feature)) {
                            var singleFeatureInfo = {};
                            singleFeatureInfo['val'] =  imgData['data'][feature];
                            singleFeatureInfo['category'] = featureLookup[feature]['category'];
                            singleFeatureInfo['min'] = featureLookup[feature]['minval'];
                            singleFeatureInfo['max'] = featureLookup[feature]['maxval'];
                            queryBuilder[feature] = singleFeatureInfo
                        }
                    }

                    $scope.queryBuilder = queryBuilder

                })

            }

        )
    }

]);





