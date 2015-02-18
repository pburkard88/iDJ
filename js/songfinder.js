angular.module('songfinder', ['spotify'])
	/*
	.config(function (SpotifyProvider) {
    	SpotifyProvider.setClientId('171b23b89d5445eeb63a3757a6d446b1');
    	SpotifyProvider.setRedirectUri('http://example.com/callback.html');
    	SpotifyProvider.setScope('playlist-read-private');
  	})
  	*/
	.controller('SearchController', ['$scope', 'Spotify', function($scope, Spotify) {
		$scope.search_url_base = 'https://api.spotify.com/v1/search?q=';
		$scope.search_term = '';
		$scope.search_results = [];
		$scope.searchTrack = function () {
      		Spotify.search($scope.search_term, 'track').then(function (data) {
        		$scope.search_results = data.tracks.items.filter(function(item) {
        			for (var i=0; i< $scope.selected_tracks.length; i++) {
        				if ($scope.selected_tracks[i].id === item.id) {
        					return false;
        				}
        			}
        			return true;
        		});
      		});
      		return $scope.search_results;
    	};
    	
    	$scope.selectOrderProp = 'name'
    	$scope.selected_tracks = [];
    	
    	$scope.selectTrack = function(id) {
    		console.log("Selecting song " + id);
    		var searchIndex = $scope.search_results.map(function(x) {return x.id; }).indexOf(id);
    		track_to_add = $scope.search_results[searchIndex];
    		$scope.selected_tracks.push(track_to_add);
    		$scope.searchTrack()
    	};
    	
    	$scope.removeTrack = function(id) {
    		console.log("Deselecting song " + id);
    		var selectedIndex = $scope.selected_tracks.map(function(x) {return x.id; }).indexOf(id);
    		$scope.selected_tracks.splice(selectedIndex, 1);
    		// Update search results
    		$scope.searchTrack();
		};
	}]);
			
			