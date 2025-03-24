'use strict';


angular.module('widgets')
  .factory('wActions', ['wRequests', '$q',
    function(wRequests, $q){
      var self = this;
      var joinUrl = function(part1, part2){
        var url = '';
        if (part1.endsWith('/') && part2.startsWith('/')){url = part1 + part2.substring(1, part2.length);}
        else if ((!part1.endsWith('/') && !part2.startsWith('/'))) {url = part1 + '/' + part2;}
        else {apiAction = server + apiAction;}
        if (!url.endsWith('/')) {url += '/';}
        return url
      };
      self.promise = {
        user: function(user){
          var resolvedUser = user;
          return resolvedUser;
        },
        permissions: function(permissions){
          var promesedPermissions = new Array();
          _.each(permissions, function(permission){
              var promisedPermission = $q.defer();
              wRequests.get(permission)
                .success(function(response, status, headers, config){
                  promisedPermission.resolve({
                    codename: response.codename,
                    status: status,
                    error: null
                  });
                })
                .error(function(response, status, headers, config){
                  promisedPermission.reject({
                    codename: null,
                    status: status,
                    error: response.error
                  });
                });
              promesedPermissions.push(promisedPermission.promise);
            });
          return promesedPermissions;
        },
        groups: function(groups){
          var promisedGroups = new Array();
          _.each(groups, function(group){
              var promiseedGroup = $q.defer();
              wRequests.get(group)
                .success(function(response, status, headers, config){
                  promiseedGroup.resolve({
                    name: response.name,
                    permissions: response.permissions,
                    status: status,
                    error: null
                  });
                })
                .error(function(response, status, headers, config){
                  promiseedGroup.reject({
                    group: null,
                    pwemissions: null,
                    status: status,
                    error: response
                  });
                });
              promisedGroups.push(promiseedGroup.promise);
            });
          return promisedGroups;
        }
      };
      self.actions = {
        login: function(email, password, apiAction){
          var server = wRequests.getServer();
          apiAction = joinUrl(server, apiAction);
          var params = {
            email: email,
            password: password
          }
          var deferred = $q.defer();
          wRequests.post(apiAction, params)
            .success(function(data, status, headers, config){
              deferred.resolve({
                user: data,
                status: status,
                error: null
              });
            })
            .error(function(data, status, headers, config){
              deferred.reject({
                user: null,
                status: status,
                error: data.error
              });
            });
          return deferred.promise;
        },
        resolveUser: function(user){
          var promisedPermissions = self.promise.permissions(user.user_permissions);
          var promisedGroups = self.promise.groups(user.groups);
          user.permissions = new Array();
          var promisedUser = $q.defer();
          $q.all(promisedPermissions)
            .then(
              function(permissions){
                user.permissions.push(permissions);
                user.user_permissions = permissions;
                $q.all(promisedGroups)
                  .then(
                    function(groups) {
                      _.each(groups, function(group){
                        var promisedPermissions = self.promise.permissions(group.permissions);
                        $q.all(promisedPermissions)
                          .then(
                            function(permissions){
                              group.permissions = permissions;
                              user.permissions.push(permissions);
                              user.permissions = _.uniq(_.flatten(user.permissions), false, 'codename');
                              user.groups = groups;
                              promisedUser.resolve(user);
                            }
                          );
                      });
                    });
              });
          return promisedUser.promise;
        },
        setCookies: function(response){
          console.log(response);
          return true;
        },
        setConfig: function(response){
          console.log(response);
          return true;
        },
        logout: function(){
          console.log('logout');
        }
      }
      return function(){
        return self.actions;
      };
    }]);