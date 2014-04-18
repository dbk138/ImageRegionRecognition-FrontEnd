'use strict';
/* Controllers */

var featureQueryControllers = angular.module('featureQueryControllers', []);

featureQueryControllers.controller('LocationListCtrl', function($scope, LocationLookupService) {
   $scope.locations = LocationLookupService.query();
});

featureQueryControllers.controller('sysLogCtrl', function($scope, $http) {
	$http.get('/services/syslog').success(function(data) {
		$scope.logs = data;
	});
});

featureQueryControllers.controller('FeatureListCtrl', function($scope, $http) {
    $http.get('data/featureLookup.json').success(function(data) {
        $scope.features = data;
    });
});

featureQueryControllers.controller('LocaleCtrl', function($scope, Locale) {
		Locale.getLocations().then(function(locations) {
			$scope.loc = locations;
		});
});

featureQueryControllers.controller('autocompleteCtrl' , function ($scope, $http) {
    var words = ['Area','Centroid','EulerNumber','BoundingBox', 'Extent','Perimeter','Orientation', 'ConvexArea','FilledArea','Eccentricity','MajorAxisLength',
            'Solidity','EquivDiameter','MinorAxisLength'];
    /*$http.get('data/featureLookup.json').success(function(data) {
        for(var key in data) {
            words.push(key);
            //words.push(data[key].category);
        }
        words.sort();
    });*/
    $scope.tags = "";
    $scope.availableTags = words;
	
	$scope.errors = [];
    $scope.msgs = [];
	
	$scope.submitQuery = function() {
	
		 $scope.errors.splice(0, $scope.errors.length); // remove all error messages
		 $scope.msgs.splice(0, $scope.msgs.length);
		 
		 var img = "C:\\Users\\geoimages\\angular-seed\\app\\images\\" + $scope.imageName.replace('_','\\');
		 var lcImage = "C:\\Users\\geoimages\\angular-seed\\app\\images\\" + $scope.imageName.replace('_','\\').replace('.jpg','LC.jpg');
		 var dir = "C:\\Users\\geoimages\\angular-seed\\app\\images\\" + $scope.imageName.substring(0, $scope.imageName.indexOf('_')) + "\\\\";		
			
		$http.post('/services/query', {
			'imgName': img,
			'lcImageName': lcImage,
			'queryString': $scope.query,
			'directory': dir
		}).success(function(data, status, headers, config) {
			$scope.msgs.push("Your query was submitted successfully.");	
		}).error(function() {
			$scope.errors.push(status);
		});
	};
	
});
/*
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
*/

featureQueryControllers.controller('ImageCtrl2', ['$scope', '$http', '$routeParams','ImageService','FeatureLookupService', 'LocationLookupService',
    function($scope, $http, $routeParams, ImageService, FeatureLookupService, LocationLookupService) {

        $scope.imageName = $routeParams.imageName;
		
		var nameString = $scope.imageName;
		
		var name = nameString.substring(0, nameString.indexOf("_"));
		
		$scope.locations = LocationLookupService.query();
		
		LocationLookupService.query(function(locations) {
			for(var i = 0; i<locations.length; i++) {
				if(locations[i].name == name) {
					$scope.location = locations[i];
				}
			}
		});
		
        /*$http.get('/services/getlocations').then(function(location) {
			for(var i = 0; i<location.length; i++) {
				if($scope.imageName = location['name']) {
					$scope.location = location['name'];
				}
			}
		});
		*/
		//$scope.location = {"images":[{"name":"Alderwood Lake SE/Alderwood Lake SE_w004_h012.jpg"}],"name":"Alderwood Lake SE"}; 
        

         ImageService.get({imageName:$scope.imageName.concat('.json')}
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
                    //if(summaryInfo[key] === maxValue.toString()) {
                        //element = key;
                        //value = (parseFloat(summaryInfo[key]) * 100).toFixed(2);
				summaryInfo[key] = (parseFloat(summaryInfo[key]) * 100).toFixed(2);
                    //}
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





