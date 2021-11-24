from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class Movie(db.Model):
    __tablename__ = 'marketler'  # creating a table name
    # this is the primary key
    market_id = db.Column(db.Integer, primary_key=True)
    market_adi = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    aciklama = db.Column(db.String(80), nullable=False)
    sayfa_sayisi = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'market_id': self.market_id, 'market_adi': self.market_adi,
                'aciklama': self.aciklama, 'sayfa_sayisi': self.sayfa_sayisi}
        # this method we are defining will convert our output to json

    def add_movie(_market_adi, _aciklama, _sayfa_sayisi):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_movie = Movie(market_adi=_market_adi,
                          aciklama=_aciklama, sayfa_sayisi=_sayfa_sayisi)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_movies():
        '''function to get all movies in our database'''
        return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_market_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Movie.json(Movie.query.filter_by(market_id=_market_id).first())]
        # Movie.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_movie(_market_id, _market_adi, _aciklama, _sayfa_sayisi):
        '''function to update the details of a movie using the id, title,
        year and genre as parameters'''
        movie_to_update = Movie.query.filter_by(market_id=_market_id).first()
        movie_to_update.title = _market_adi
        movie_to_update.year = _aciklama
        movie_to_update.genre = _sayfa_sayisi
        db.session.commit()

    def delete_movie(_market_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Movie.query.filter_by(market_id=_market_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database
