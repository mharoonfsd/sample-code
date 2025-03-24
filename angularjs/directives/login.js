'use strict';


angular.module('widgets')
  .directive('wLogin', function(){
    return{
      restrict: 'EA',
      templateUrl: 'app/components/templates/login.html',
      scope: {
        action: '=',
        apiAction: '=',
        class: '=',
      },
      controller: 'wLoginCtrl'
    }
  });