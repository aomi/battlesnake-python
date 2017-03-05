from node import *
import bottle
#from bottle import request, route, run, template, post, default_app, static_file
from astar import calculatePathWeight
import os
import random

debug = True

board = {}

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.route('/')
def index():
    return 'server is running properly'


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

    return {
        'color': '#66CCFF',
        'taunt': 'Forming, Storming, Norming, Performing',
        'head_url': head_url,
        'name': 'Wild\'s Disciples'
    }


@bottle.post('/move')
def move():
    # initialize the node list with received data
    data = bottle.request.json
    ourID = data['you']
    #clear the old board state to prepare it for the new population
    board[data['game_id']].clear()
    ourHeadNode = board[data['game_id']].getNode(0,0)

    # add snakes into NodeList
    for snake in data['snakes']:
        snake_id = snake['id']
        head = True
        for a in snake['coords']:
            if(head):
                if(snake['id'] == ourID):
                    ourHeadNode = board[data['game_id']].getNode(a[0],a[1])

                board[data['game_id']].changeContent(a[0],a[1],"wall") #IMPLEMENT TO OTHERHEAD
                head = False
            else:
                board[data['game_id']].changeContent(a[0],a[1],"wall")

    #add the food into the node list
    for food in data['food']:
        board[data['game_id']].changeContent(food[0],food[1],"food")

    # gives each node a weighting so the algorithm knows the relative safety of each node.
    board[data['game_id']].weight()

    for y in range(MAPSIZEY):
        s = ''
        for x in range(MAPSIZEX):                   ####TESTING
            if(board[data['game_id']].getList()[x][y].content == 'open'):
                s += 'O'
            else:
                s += 'X'
        print s

    #a* call happens here.
    eachCherry = []

    for food in data['food']:
        if debug: print("current food:", food)
        if debug: print("head: ", ourHeadNode.x, ourHeadNode.y)
        if debug: tempNode = board[data['game_id']].getNode(food[0], food[1])
        if debug: print("food icon: ", tempNode.x, tempNode.y)
        eachCherry.append(calculatePathWeight(ourHeadNode, tempNode))
        if debug: print("current EachCherry:", eachCherry)

    currentSmallestCherry = eachCherry[0]

    for cherry in eachCherry[:1]:
        if(currentSmallestCherry[0] > eachCherry[0]):
            currentSmallestCherry = cherry

    return {
        'move': currentSmallestCherry[1],
        'taunt': 'Forming, Storming, Norming, Performing'
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
