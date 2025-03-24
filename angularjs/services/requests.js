'use strict';


angular.module('widgets')
  .service('wRequests', ['$sce', '$http', '$location', '$cookieStore', '$cookies',
    function($sce, $http, $location, $cookieStore, $cookies){
      return {
        getServer: function(){
          var protocol = $location.protocol();
          var host = $location.host();
          var port = $location.port();
          var server = protocol + '://' + host;
          if (port && parseInt(port)) {
            server += ':' + port + '/'
          }
          else {
            server += '/'
          }

          return server
        },
        getThisUrl: function(){
         return $location.absUrl();
        },
        get: function(url, params){
          if (!url.endsWith('/')){url += '/?';}
          else {url += '?';}
          _.each(params, function(value, key){
            url += key + '=' + value + '&';
          })
          if (url.endsWith('&') || url.endsWith('?')){
            url = url.substring(0, url.length-1);
          }
          return $http({
            method: 'GET',
            url: url
          });
        },
        post: function(url, params){
          var transformation = function(obj){
            var str = [];
            for (var p in obj)
            str.push(encodeURIComponent(p) + '=' + obj[p]);
            return str.join('&');
          }
          return $http({
            method: 'POST',
            url: url,
            data: params,
            transformRequest: transformation
          });
        },
        put: function(url, params){
          
        },
        patch: function(url, params){
          
        },
        delete: function(url, params){
          
        }
      }
    }]);