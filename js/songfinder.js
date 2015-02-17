/*angular.module('songfinder', ['spotify', 'ngResource'])
	.config(function (SpotifyProvider) {
    	SpotifyProvider.setClientId('171b23b89d5445eeb63a3757a6d446b1');
    	SpotifyProvider.setRedirectUri('http://example.com/callback.html');
    	SpotifyProvider.setScope('playlist-read-private');
  	})
  	*/
angular.module('songfinder', ['spotify'])
	.controller('SearchController', ['$scope', 'Spotify', function($scope, Spotify) {
		$scope.search_url_base = 'https://api.spotify.com/v1/search?q=';
		$scope.search_term = '';
		$scope.search_results = [];
		$scope.searchTrack = function () {
      		Spotify.search($scope.search_term, 'track').then(function (data) {
        		$scope.search_results = data.tracks.items;
      		});
      		return $scope.search_results;
    	};
	}]
);
			
			