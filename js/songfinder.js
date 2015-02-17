angular.module('songfinder', [])
	.controller('SearchController', ['$scope', '$http', function($scope, $http) {
		$scope.search_url_base = 'https://api.spotify.com/v1/search?q=';
		$scope.search_term = '';
		$scope.search_results = [];
		$scope.doSearch = function() {
			$http.get($scope.search_url_base + $scope.search_term + '&type=track').success(function(data) {
				$scope.results = data.results;
			});
			return $scope.results;
		};
	}]
);
			
			