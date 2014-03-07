'use strict';

/* Controllers */

var featureQueryControllers = angular.module('featureQueryControllers', []);

featureQueryControllers.controller('LocationListCtrl', function($scope, $http) {
    $http.get('data/locationLookup.json').success(function(data) {
        $scope.locations = data;
    });

});



featureQueryControllers.controller('ImageCtrl2', ['$scope','$routeParams','ImageService','FeatureLookupService',
    function($scope,$routeParams, ImageService,FeatureLookupService) {

        $scope.imageName = $routeParams.imageName

         ImageService.get({imageName:$scope.imageName.replace('/','_').concat('.json')}
            ,  //success function
            function (imgData) {

                var summaryInfo ={};
                summaryInfo['URBAN/DEVELOPED']=imgData['data']['L1_100']
                summaryInfo['AGRICULTURE']= imgData['data']['L1_110']
                summaryInfo['GRASSLAND']=imgData['data']['L1_150']
                summaryInfo['FOREST']=imgData['data']['L1_160']
                summaryInfo['OPEN WATER']=imgData['data']['L1_200']
                summaryInfo['WETLAND ']=imgData['data']['L1_210']
                summaryInfo['BARREN']=imgData['data']['L1_240']
                summaryInfo['SHRUBLAND']=imgData['data']['L1_250']
                summaryInfo['CLOUD COVER']=imgData['data']['L1_255']
                $scope.summaryInfo = summaryInfo

                // lets get the feature lookup data here.
                //  notice i'm still inside the success function of the first service call.
                // Instead this functionality of marshalling the async calls should be done via promises.
                // but i don't know heck about promises as yet.

                FeatureLookupService.get({},
                // success function
                function(featureLookup) {
                    var queryBuilder = {}
                    for ( var feature in (imgData['data'])) {
                        if (imgData['data'].hasOwnProperty(feature)) {
                            var singleFeatureInfo = {}
                            singleFeatureInfo['val'] =  imgData['data'][feature]
                            singleFeatureInfo['min'] = featureLookup[feature]['minval']
                            singleFeatureInfo['max'] = featureLookup[feature]['maxval']
                            queryBuilder[feature] = singleFeatureInfo
                        }
                    }

                    $scope.queryBuilder = queryBuilder

                })


            }

        )
    }

]);

featureQueryControllers.controller('ImageCtrl', ['$scope', '$routeParams','$http',
    function($scope, $routeParams, $http) {
        // set the image name requested by client
        $scope.imageName = $routeParams.imageName;

        // get the image info.
        $http.get('data/images/'.concat($scope.imageName.replace('/','_').concat('.json'))).success(function(data) {
            //var imgData = data
            $scope.imgData = data
            var summaryInfo ={};
            summaryInfo['URBAN/DEVELOPED']=$scope.imgData['data']['L1_100']
            summaryInfo['AGRICULTURE']=$scope.imgData['data']['L1_110']
            summaryInfo['GRASSLAND']=$scope.imgData['data']['L1_150']
            summaryInfo['FOREST']=$scope.imgData['data']['L1_160']
            summaryInfo['OPEN WATER']=$scope.imgData['data']['L1_200']
            summaryInfo['WETLAND ']=$scope.imgData['data']['L1_210']
            summaryInfo['BARREN']=$scope.imgData['data']['L1_240']
            summaryInfo['SHRUBLAND']=$scope.imgData['data']['L1_250']
            summaryInfo['CLOUD COVER']=$scope.imgData['data']['L1_255']
            $scope.summaryInfo = summaryInfo
        });

        // now lets get the features.
        $http.get('data/featureLookup.json').success(function(data) {
            var featureLookup = data
            var queryBuilder = {}

            for ( var feature in ($scope.imgData['data'])) {
                if ($scope.imgData['data'].hasOwnProperty(feature)) {
                    var singleFeatureInfo = {}
                    singleFeatureInfo['val'] =  $scope.imgData['data'][feature]
                    singleFeatureInfo['min'] = featureLookup[feature]['minval']
                    singleFeatureInfo['max'] = featureLookup[feature]['maxval']
                    queryBuilder[feature] = singleFeatureInfo

                }
            }

            $scope.queryBuilder = queryBuilder

        });



    }]);


