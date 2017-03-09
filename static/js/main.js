var app = angular.module('bandtracker', ['ngResource']);
app.config(function($httpProvider, $resourceProvider){
    $resourceProvider.defaults.stripTrailingSlahes = false;
});

app.controller('BandData', function ($scope, $http) {
    $scope.find = function () {
        console.log(this.search_item);
        var item_no_space = this.search_item.split(' ').join('')
        console.log(Flask.url_for('home') +'gigs?'+ item_no_space)
        $http.get(Flask.url_for('home') +'gigs?'+ item_no_space).success(function (response) {
                $scope.locations = response.data;
                if (typeof $scope.locations == 'object')
                    console.log($scope.locations);
                else
                    console.log('Not actually an object, it really is ', typeof $scope.greeting);
            });
    };
});
