'use strict';


angular.module('widgets')
  .controller('wLoginCtrl', ['$scope', 'wActions',
    function($scope, wActions){
      $scope.methods = {
        login: function (){
          $scope.error = null;
          var actions = new wActions;
          var setUser = function(){
            actions.login(
              $scope.email,
              $scope.password,
              $scope.apiAction
            )
              .then(
                function(response){
                  var setCookiesAndConfig = function(){
                    var resolveUser = actions.resolveUser(response.user)
                      .then(
                        function(resolved){
                          $scope.user = resolved;
                          response.user = resolved;
                          actions.setCookies(response);
                          actions.setConfig(response);
                        },
                        function(unResolved){
                          $scope.user = unResolved;
                        });
                  };
                  setCookiesAndConfig();
                  var loginForm = document.getElementById('w-login-form');
                    loginForm.action = $scope.action;
                    //loginForm.submit();
                },
                function (response){
                  $scope.error = response.status + ': ' + response.error;
                }
              );
          };
          setUser();
       }
      };
    }]);