from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


# class User:
#     '''
#     Movie class to define Movie Objects
#     '''

    # def __init__(self,id,title,overview,poster,vote_average,vote_count):
    #     self.id = id
    #     self.title = title
    #     self.overview = overview
    #     self.poster = "https://image.tmdb.org/t/p/w500/" + poster
    #     self.vote_average = vote_average
    #     self.vote_count = vote_count



    
   
    # @classmethod
    # def get_reviews(cls,id):

    #     response = []

    #     for review in cls.all_reviews:
    #         if review.movie_id == id:
    #             response.append(review)

    #     return response
    