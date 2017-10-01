'use strict';

/* Controllers */


function HomeController($scope, PLCList)
{
	var topicResults = PLCList.get({}, function(data){
		$scope.data = data;
	});

	$scope.moveTo = function(link)
	{
		window.location = link;
	}
}

function StatusController($scope, $routeParams, $timeout, PLCStatus)
{
	var statusResults = PLCStatus.get({plc: $routeParams.plc}, function(data) {
        $scope.data = data;
    });


	function tick() {
		var statusResults = PLCStatus.get({plc: $routeParams.plc}, function(data) {
	        $scope.data = data;
	        if($scope.no_blink)
	        {
	        	for(var i=0; i < $scope.no_blink.length; i++)
	        	{
	        		var key = $scope.no_blink[i];
	        		if($scope.data.invariants[key].color != 'card hoverable dapp-card red accent-3 blink')
	        		{
	        			$scope.no_blink.splice(i, 1);
	        		}
	        		else
	        		{
	        			$scope.data.invariants[key].color = 'card hoverable dapp-card red accent-3';
	        		}
	        	}
	        }
	    });
		var timer = $timeout(tick, 7000);
	}

	$scope.removeBlink = function(key)
	{
		if ($scope.data.invariants[key].color == 'card hoverable dapp-card red accent-3 blink')
		{
			$scope.data.invariants[key].color = 'card hoverable dapp-card red accent-3';

			if($scope.no_blink)
			{
				$scope.no_blink.push(key);
			}
			else
			{
				$scope.no_blink = [key];
			}

		}
	}

	tick();

	$scope.$on("destroy", function()
	{
		if(timer) {
			$timeout.cancel(timer);
		}
	});
}

