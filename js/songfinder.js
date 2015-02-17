angular.module('songfinder', ['ngResource'])
	.controller('SearchController', ['$scope', '$resource', function($scope, $resource) {
		$scope.search_url_base = 'https://api.spotify.com/v1/search?q=';
		$scope.search_term = '';
		$scope.search_results = [];
		$scope.doSearch = function() {
			/*
			search_url = $scope.search_url_base + $scope.search_term + '&type=track';
			$http.get($scope.search_url_base + $scope.search_term + '&type=track').success(function(data) {
				$scope.search_results = data.results;
			});
			*/
			search_url = $scope.search_url_base + $scope.search_term + '&type=track';
			rest_search = $resource(search_url, {}, {
				query: {method: 'GET', params:{}, isArray: false}
				});
			$scope.search_results = rest_search.query();
			return $scope.search_results;
		};
	}]
);
			
			