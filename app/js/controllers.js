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

featureQueryControllers.controller('queryLogCtrl', function($scope, $http) {
	$http.get('/services/querylog').success(function(data) {
		$scope.logs = data;
	});
});

featureQueryControllers.controller('testLogCtrl', function($scope, $http) {
	$http.get('/services/unittestlog').success(function(data) {
		$scope.logs = data;
	});
});

featureQueryControllers.controller('FeatureListCtrl', function($scope, $http) {
    $http.get('data/featureLookup.json').success(function(data) {
        $scope.features = data;
    });
});

featureQueryControllers.controller('autocompleteCtrl' , function ($scope, $http) {
    var words = ['Area','Centroid','EulerNumber','BoundingBox', 'Extent','Perimeter','Orientation', 'ConvexArea','FilledArea','Eccentricity','MajorAxisLength',
            'Solidity','EquivDiameter','MinorAxisLength'];

    $scope.tags = "";
    $scope.availableTags = words;
	$scope.processed = false;
	$scope.errors = [];
    $scope.msgs = [];
	
	$scope.submitQuery = function() {
		 
		 $scope.errors.splice(0, $scope.errors.length); // remove all error messages
		 $scope.msgs.splice(0, $scope.msgs.length);
		 
		 document.getElementById("submitQuery").disabled=true;
		 $scope.submitted = "Processing query, please wait...";
		 
		 var img = "C:\\Users\\geoimages\\angular-seed\\app\\images\\" + $scope.imageName.replace('_','\\');
		 var lcImage = "C:\\Users\\geoimages\\angular-seed\\app\\images\\" + $scope.imageName.replace('_','\\').replace('.jpg','LC.jpg');
		 var dir = new Date().getTime() + "//";		
			
		$http.post('/services/query', {
			'imgName': img,
			'lcImageName': lcImage,
			'queryString': $scope.query,	
			'dir': dir
		}).success(function(data, status, headers, config) {
			$scope.msgs.push("Your query was submitted successfully.");	
			$scope.processed = true;
			$scope.checkered = dir + "checkeredImage.jpg#" + new Date().getTime();
			$scope.region = dir + "regionsImage.jpg#" + new Date().getTime();
			
			document.getElementById("submitQuery").disabled=false;
			$scope.submitted = "";
		}).error(function() {
			$scope.errors.push(status);
			document.getElementById("submitQuery").disabled=false;
			$scope.submitted = "";
		});
	};
	
});

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
					summaryInfo[key] = (parseFloat(summaryInfo[key]) * 100).toFixed(2);
                }


            }

        )
    }

]);
