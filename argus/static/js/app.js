'use strict';

angular.module('AngularFlask', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/list.html',
			controller: HomeController
		})
		.when('/status/:plc',{
			templateUrl: '/static/partials/statuslist.html',
			controller: StatusController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
	.filter('clean_date', function() {
		return function(input) {
			if(input != undefined)
				return input.replace('GMT', '');
			else
				return '';
		}
	})
	.filter('clean_invariant', function() {
		return function(input) {
			if(input != undefined)
				return input.replace('CPS_ALID_', '');
			else
				return '';
		}
	});
