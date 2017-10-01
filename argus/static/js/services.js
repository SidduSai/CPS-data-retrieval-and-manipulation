'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('PLCList', function($resource){
		return $resource('/api', {}, {
			query : {
				method: 'GET',
			}
		})
	})
	.factory('PLCStatus', function($resource){
		return $resource('/api/status/:plc', {}, {
			query : {
				method: 'GET',
				params: {'plc': ''}
			}
		})
	})
;



