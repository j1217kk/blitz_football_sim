from flask import Blueprint, jsonify, request
from fbsim.models import db, Player, player_schema, players_schema

api = Blueprint('api', __name__, url_prefix= '/api' )

@api.route('/players/<token>', methods=['POST'])
def add_player(token):
    starting=request.json['starting']
    player_name=request.json['player_name']
    position=request.json['position']
    team=request.json['team']
    total_standard=request.json['total_standard']
    total_ppr=request.json['total_ppr']
    total_hppr=request.json['total_hppr']
    szn_pass_y=request.json['szn_pass_y']
    szn_rush_y=request.json['szn_rush_y']
    szn_rcv_y=request.json['szn_rcv_y']
    szn_pass_td=request.json['szn_pass_td']
    szn_rush_td=request.json['szn_rush_td']
    szn_rcv_td=request.json['szn_rcv_td']


    if Player.query.filter_by(player_name=player_name, token=token).first():
        return jsonify({'message': f'{player_name} is already part of your fantasy roster. Try a different player.'})
    else:
        player = Player(player_name, position, team, total_standard, total_ppr, total_hppr, szn_pass_y, szn_rush_y, szn_rcv_y, szn_pass_td, szn_rush_td, szn_rcv_td, starting)

        db.session.add(player)
        db.session.commit()

        response = player_schema.dump(player)

        return jsonify(response)

@api.route('/players/<token>', methods=['GET'])
def get_players(token):
    players = Player.query.filter_by(token=token).all()
    response = players_schema.dump(players)

    return jsonify(response)


@api.route('/players/<token>/<id>', methods=['PUT', 'POST'])
def update_player(token, id):
    player = Player.query.get(id)
    player.starting=request.json['starting']
    db.session.commit()
    response = player_schema.dump(player)

    return jsonify(response)

@api.route('/players/<token>/<id>', methods=['DELETE'])
def delete_player(token, id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    response=player_schema.dump(player)
    return jsonify(response)