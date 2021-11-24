from movies import *


# route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    '''Function to get all the movies in the database'''
    data = Movie.get_all_movies()
    if not data:
        success = 0
    else:
        success = 1
    return jsonify({'marketler': Movie.get_all_movies(), "success": success})


# route to get movie by id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)


# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    Movie.add_movie(request_data["market_adi"], request_data["aciklama"],
                    request_data["sayfa_sayisi"])
    response = Response("Movie added", 201, mimetype='application/json')
    return response


# route to update movie with PUT method
@app.route('/movies/<int:market_id>', methods=['PUT'])
def update_movie(market_id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Movie.update_movie(
        id, request_data['market_adi'], request_data['aciklama'], request_data['sayfa_sayisi'])
    response = Response("Movie Updated", status=200,
                        mimetype='application/json')
    return response


# route to delete movie using the DELETE method
@app.route('/movies/<int:market_id>', methods=['DELETE'])
def remove_movie(market_id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(market_id)
    response = Response("Movie Deleted", status=200,
                        mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)
