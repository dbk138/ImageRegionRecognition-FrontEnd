'use strict';

/* Controllers */

var featureQueryControllers = angular.module('featureQueryControllers', []);

featureQueryControllers.controller('LocationListCtrl', function($scope, $http) {
    $http.get('data/locationLookup.json').success(function(data) {
        $scope.locations = data;
    });

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

featureQueryControllers.controller( 'testCtrl'  ,function ($scope) {
    $scope.tags = "";
    $scope.availableTags = ["area_kurtosis","area_mean","area_median","area_quantile250","area_quantile975","area_skewness","area_std","boundingbox_kurtosis","boundingbox_mean","boundingbox_median","boundingbox_quantile250","boundingbox_quantile975","boundingbox_skewness","boundingbox_std","centroid_kurtosis","centroid_mean","centroid_median","centroid_quantile250","centroid_quantile975","centroid_skewness","centroid_std","color_b_kurtosis","color_b_mean","color_b_median","color_b_quantile250","color_b_quantile975","color_b_skewness","color_b_std","color_contrast_1","color_contrast_4","color_contrast_9","color_correlation_1","color_correlation_4","color_correlation_9","color_energy_1","color_energy_4","color_energy_9","color_entropy","color_g_kurtosis","color_g_mean","color_g_median","color_g_quantile250","color_g_quantile975","color_g_skewness","color_g_std","color_gray_kurtosis","color_gray_mean","color_gray_median","color_gray_quantile250","color_gray_quantile975","color_gray_skewness","color_gray_std","color_h_kurtosis","color_h_mean","color_h_median","color_h_quantile250","color_h_quantile975","color_h_skewness","color_h_std","color_homogeneity_1","color_homogeneity_4","color_homogeneity_9","color_r_kurtosis","color_r_mean","color_r_median","color_r_quantile250","color_r_quantile975","color_r_skewness","color_r_std","color_s_kurtosis","color_s_mean","color_s_median","color_s_quantile250","color_s_quantile975","color_s_skewness","color_s_std","color_v_kurtosis","color_v_mean","color_v_median","color_v_quantile250","color_v_quantile975","color_v_skewness","color_v_std","convexarea_kurtosis","convexarea_mean","convexarea_median","convexarea_quantile250","convexarea_quantile975","convexarea_skewness","convexarea_std","eccentricity_kurtosis","eccentricity_mean","eccentricity_median","eccentricity_quantile250","eccentricity_quantile975","eccentricity_skewness","eccentricity_std","equivdiameter_kurtosis","equivdiameter_mean","equivdiameter_median","equivdiameter_quantile250","equivdiameter_quantile975","equivdiameter_skewness","equivdiameter_std","eulernumber_kurtosis","eulernumber_mean","eulernumber_median","eulernumber_quantile250","eulernumber_quantile975","eulernumber_skewness","eulernumber_std","extent_kurtosis","extent_mean","extent_median","extent_quantile250","extent_quantile975","extent_skewness","extent_std","filledarea_kurtosis","filledarea_mean","filledarea_median","filledarea_quantile250","filledarea_quantile975","filledarea_skewness","filledarea_std","l1_100","l1_110","l1_160","l1_210","l1_240","l1_250","l1_255","majoraxislength_kurtosis","majoraxislength_mean","majoraxislength_median","majoraxislength_quantile250","majoraxislength_quantile975","majoraxislength_skewness","majoraxislength_std","minoraxislength_kurtosis","minoraxislength_mean","minoraxislength_median","minoraxislength_quantile250","minoraxislength_quantile975","minoraxislength_skewness","minoraxislength_std","orientation_kurtosis","orientation_mean","orientation_median","orientation_quantile250","orientation_quantile975","orientation_skewness","orientation_std","perimeter_kurtosis","perimeter_mean","perimeter_median","perimeter_quantile250","perimeter_quantile975","perimeter_skewness","perimeter_std","phase_congruency_ft_kurtosis","phase_congruency_ft_mean","phase_congruency_ft_median","phase_congruency_ft_quantile250","phase_congruency_ft_quantile975","phase_congruency_ft_skewness","phase_congruency_ft_std","phase_congruency_max_moment_kurtosis","phase_congruency_max_moment_mean","phase_congruency_max_moment_median","phase_congruency_max_moment_quantile250","phase_congruency_max_moment_quantile975","phase_congruency_max_moment_skewness","phase_congruency_max_moment_std","phase_congruency_min_moment_kurtosis","phase_congruency_min_moment_mean","phase_congruency_min_moment_median","phase_congruency_min_moment_quantile250","phase_congruency_min_moment_quantile975","phase_congruency_min_moment_skewness","phase_congruency_min_moment_std","phase_congruency_noise_thresh","phase_congruency_orientation_kurtosis","phase_congruency_orientation_mean","phase_congruency_orientation_median","phase_congruency_orientation_quantile250","phase_congruency_orientation_quantile975","phase_congruency_orientation_skewness","phase_congruency_orientation_std","solidity_kurtosis","solidity_mean","solidity_median","solidity_quantile250","solidity_quantile975","solidity_skewness","solidity_std","texture_autoc_1","texture_autoc_2","texture_contr_1","texture_contr_2","texture_corrm_1","texture_corrm_2","texture_corrp_1","texture_corrp_2","texture_cprom_1","texture_cprom_2","texture_cshad_1","texture_cshad_2","texture_denth_1","texture_denth_2","texture_dissi_1","texture_dissi_2","texture_dvarh_1","texture_dvarh_2","texture_energ_1","texture_energ_2","texture_entro_1","texture_entro_2","texture_homom_1","texture_homom_2","texture_homop_1","texture_homop_2","texture_idmnc_1","texture_idmnc_2","texture_indnc_1","texture_indnc_2","texture_inf1h_1","texture_inf1h_2","texture_inf2h_1","texture_inf2h_2","texture_maxpr_1","texture_maxpr_2","texture_savgh_1","texture_savgh_2","texture_senth_1","texture_senth_2","texture_sosvh_1","texture_sosvh_2","texture_svarh_1","texture_svarh_2","weightedcentroid_kurtosis","weightedcentroid_mean","weightedcentroid_median","weightedcentroid_quantile250","weightedcentroid_quantile975","weightedcentroid_skewness","weightedcentroid_std"];
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


featureQueryControllers.controller('ImageCtrl2', ['$scope','$routeParams','ImageService','FeatureLookupService',
    function($scope,$routeParams, ImageService,FeatureLookupService) {

        $scope.imageName = $routeParams.imageName;

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
                var maxValue = Math.max.apply(this, max);

                for( var key in summaryInfo) {
                    if(summaryInfo[key] === maxValue.toString()) {
                        element = key;
                    }
                }

                $scope.classification = element;

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





