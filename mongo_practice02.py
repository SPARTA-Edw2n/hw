from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':'월-E'})
target_star =target_movie['star']
print(target_star)

selected_movies = list(db.movies.find({'star':target_star}))
for movie in selected_movies:
    print(movie['title'])

db.movies.update_many({'star':target_star},{'$set':{'star':0}})