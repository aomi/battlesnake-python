from node import *
from bottle import route, run, template, post, default_app, static_file
#import bottle

import os
import random

board = {}

@route('/static/<path:path>')
def static(path):
    return static_file(path, root='static/')


@route('/')
def index():
    return 'server is running properly'


@route('/debug/<id>')
def display_debug(id):
    return board[id]


@post('/start')
def start():
    #getting the data from the server at startup
    data = request.json
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
        request.urlparts.scheme,
        request.urlparts.netloc
    )

    # TODO: Do things with data

    return
    {
        'color': '#00FF00',
        'taunt': 'Forming, Storming, Norming, Performing',
        'head_url': head_url,
        'name': 'Wild\'s Disciples'
    }


@post('/move')
def move():
    # initialize the node list with received data
    data = request.json

    #clear the old board state to prepare it for the new population
    board[data['game_id']].clear()

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

    # gives each node a weighting so the algorithm knows the relative safety of each node.
    board[data['game_id']].weight()

    #a* call happens here.

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return
    {
        'move': random.choice(directions),
        'taunt': 'Forming, Storming, Norming, Performing'
    }


# Expose WSGI app (so gunicorn can find it)
application = default_app()
if __name__ == '__main__':
    run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))



"""
Numbering system for Node contents
0 = wall / impassable / snake tail (danger)
1 = open
2 = food
3 = our head
4 = other snake head
"""
