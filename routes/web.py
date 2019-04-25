"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    Get().route('/todo', 'TodoController@index'),
    Post().route('/todo', 'TodoController@store'),
    Get().route('/todo/@id/edit', 'TodoController@edit'),
    Post().route('/todo/@id/update', 'TodoController@update'),
    Post().route('/todo/@id/delete', 'TodoController@destroy'),
]
