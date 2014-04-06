'use strict';

/* Directives */
var featureQueryDirectives = angular.module('featureQueryDirectives', []);



featureQueryDirectives.directive('autocomplete', function() {
    return {
        restrict: 'A',
        require: "ngModel",
        link: function(scope, element, attrs, ngModel) {

            $(element).autocomplete({
                source: scope.availableTags,
                select: function(event, ui) {
                    scope.$apply(read(ui.item.value));
                   // console.log(ui.item.value)
                }
            });

            $(element).keypress(function(event) {
                var arr = scope.availableTags;
                var newarr = [];
                console.log($(element).val());
                if (event.which === 32) {
                    console.log("here");
                    var i = 0;
                    for (i=0;i<arr.length;i++)
                    {
                        var ns = $(element).val() + " " +arr[i];
                        newarr.push(ns);

                    }
                    $( element ).autocomplete( "option", "source", newarr );
                }
            });


            function read(value) {
                console.log("valueread " + value)
                ngModel.$setViewValue(value);

            }


        }
    };
});