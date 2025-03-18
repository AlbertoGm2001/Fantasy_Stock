from config import app,db
from models import Player,User
from flask import request,jsonify

@app.route('/players',methods=['GET'])
def get_players():
    players=Player.query.all()
    return [player.to_json() for player in players]

allowed_positions=['POR','DEF','CEN','DEL']

@app.route('/players',methods=['POST'])
def create_player():
    if request.json['position'] not in allowed_positions:
        return jsonify({'error':'Invalid position'}),400
    
    if Player.query.filter_by(player_id=request.json['player_id']).first() is not None:
        return jsonify({'error':'Player ID already exists'}),400

    player=Player(player_id=request.json['player_id'],
                    player_name=request.json['player_name'],
                    team=request.json['team'],
                    position=request.json['position'],
                    total_bids=0,
                    value=request.json['value'],#Esto se debería leer de la API del Fantasy
                    prev_scores=request.json['prev_scores'])#Esto se debería leer de la API del Fantasy
    
     
    db.session.add(player)
    db.session.commit()
    return 'Player created succesfully',201


@app.route('/players/<int:player_id>',methods=['GET'])
def get_player(player_id):
    player=Player.query.get(player_id)
    if player is None:
        return jsonify({'error':'Player not found'}),404
    return player.to_json()


@app.route('/players/<int:player_id>',methods=['PUT'])
def update_player(player_id):
    player=Player.query.get(player_id)
    if player is None:
        return jsonify({'error':'Player not found'}),404
    
    if request.json.get('position') is not None and request.json.get('position') not in allowed_positions:
        return jsonify({'error':'Invalid position.Allowed positions are: ' + ', '.join(allowed_positions),
                        'position':request.json.get('position')}),400
    
    if 'player_id' in request.json and Player.query.filter_by(player_id=request.json['player_id']).first() is not None:
        return jsonify({'error':'Player ID already exists'}),400


    player.player_name=request.json.get('player_name',player.player_name)    
    player.team=request.json.get('team',player.team)
    player.position=request.json.get('position',player.position)
    player.value=request.json.get('value',player.value)
    player.prev_scores=request.json.get('prev_scores',player.prev_scores)
    
    db.session.commit()
    
    return jsonify({'player':player.to_json(),'message':'Player updated successfully'}),200


@app.route('/players/<int:player_id>',methods=['DELETE'])
def delete_player(player_id):
    player=Player.query.get(player_id)
    if player is None:
        return jsonify({'error':'Player not found'}),404    
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message':'Player deleted successfully'}),200



@app.route('/users',methods=['GET'])
def get_users():
    users=User.query.all()
    return [user.to_json() for user in users]


@app.route('/users',methods=['POST'])
def create_user():
    if 'user_name' not in request.json:
        return jsonify({'error': 'User name is required'}), 400

    if 'user_id' in request.json:
        if User.query.filter_by(user_id=request.json['user_id']).first() is not None:
            return jsonify({'error': 'User ID already exists'}), 400
        user = User(user_id=request.json['user_id'],
                   user_name=request.json['user_name'],
                   players_bids={})
    else:
        # Let SQLAlchemy auto-generate the user_id
        user = User(user_name=request.json['user_name'],
                   players_bids={})

    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201


@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    user=User.query.get(user_id)
    if user is None:
        return jsonify({'error':'User not found'}),404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'User deleted successfully'}),200

@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user=User.query.get(user_id)
    if user is None:
        return jsonify({'error':'User not found'}),404
    user.user_name=request.get('user_name',user.user_name)
    user.players_bids=request.get('players_bids',user.players_bids)
    db.session.commit()
    return jsonify(user)


@app.route('/update_bid',methods=['PUT'])
def update_bid():
    user_id=request.json['user_id']
    player_id=request.json['player_id']
    bid_change=request.json['bid_change']
    user=User.query.get(user_id)

    if user is None:
        return jsonify({'error':'User not found'}),404
    
    player=Player.query.get(player_id)
    
    if player is None:
        return jsonify({'error':'Player not found'}),404
    
    user.players_bids[player_id]=bid_change
    player.total_bids=player.total_bids+bid_change
    db.session.commit()
    return jsonify(user)

@app.route('/get_user_bids/<int:user_id>',methods=['GET'])
def get_user_bids(user_id):
    user=User.query.get(user_id)
    if user is None:
        return jsonify({'error':'User not found'}),404
    return jsonify(user.players_bids)


if __name__ == '__main__':
    app.run(debug=True)


