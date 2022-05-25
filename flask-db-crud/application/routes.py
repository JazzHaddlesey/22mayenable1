from sqlalchemy import asc
from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name = input("New Game"))
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    deleted_game = Games.query.first()
    db.session.delete(deleted_game)
    db.session.commit()
    return deleted_game.name

@app.route('/number')
def game_count():
    number_of_games = Games.query.count()
    db.session.commit()
    return number_of_games.integer

# @app.route('/number')

# def number():

#     all_games = Games.query.all()

#     num_games= len(all_games)

#     return str(num_games)
