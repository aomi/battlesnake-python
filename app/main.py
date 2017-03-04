from node import *
import bottle
import os
import random

board = {}

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.route('/')
def index():
    return 'serving is running successfully'

@bottle.post('/start')
def start():
    #getting the data from the server at startup
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    #initializing a new board in the dictionary according to the game_id
    board[game_id] = NodeList(game_id)

    # set node class variables for the specific game board
    board[game_id].MAPSIZEX = board_width
    board[game_id].MAPSIZEY = board_height

    #connecting the board nodes together.  The board is still not populated with any data yet.
    board[game_id].connect()

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return
    {
        'color': '#00FF00',
        'taunt': 'Forming, Storming, Norming, Performing',
        'head_url': head_url,
        'name': 'Wild\'sDisciples'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    # initialize the node list with received data
    # add snakes into NodeList
    for snake in data['snakes']:
        snake_id = snake['id']
        head = false
        for a in snake['coords']:
            if(not head):
                board[data['game_id']].changeContent(a[0],a[1],snake_id)
        else:
                board[data['game_id']].content(a[0],a[1],1)

    #add the food into the node list
    for food in data['food']:
        board[data['game_id']].changeContent(food[0],food[1])


    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return
    {
        'move': random.choice(directions),
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))



"""
Numbering system for Node contents
0 = wall / impassable / snake tail (danger)
1 = open
2 = food
3 = our head
4 = other snake head
"""
