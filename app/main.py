from node import *
import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.route('/')
def index():
    return 'serving is running successfully'

@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']
    # set node class variables
    node.MAPSIZEX = board_width
    node.MAPSIZEY = board_height

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': 'Forming, Storming, Norming, Performing',
        'head_url': head_url,
        'name': 'Wild\'sDisciples'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    # initialize the node list with received data
    board = NodeList()
    # add snakes into NodeList
    for snake in data['snakes']:
        snake_id = snake['id']
        head = false
        for a in snake['coords']:
            if(not head):
                board.add(a[0],a[1],snake_id)
        else:
                board.add(a[0],a[1],1)




    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
