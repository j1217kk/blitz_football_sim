from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_marshmallow import Marshmallow



db = SQLAlchemy()
marsh = Marshmallow()

class Player(db.Model):
    id = db.Column(db.String, primary_key = True)
    starting = db.Column(db.Boolean)
    player_name = db.Column(db.String(100))
    position = db.Column(db.String(10))
    team = db.Column(db.String(100))
    total_standard = db.Column(db.Numeric(precision=10, scale=2))
    total_ppr = db.Column(db.Numeric(precision=10, scale=2))
    total_hppr = db.Column(db.Numeric(precision=10, scale=2))
    szn_pass_y = db.Column(db.Numeric(precision=10, scale=2))
    szn_rush_y = db.Column(db.Numeric(precision=10, scale=2))
    szn_rcv_y = db.Column(db.Numeric(precision=10, scale=2))
    szn_pass_td = db.Column(db.Numeric(precision=10, scale=2))
    szn_rush_td = db.Column(db.Numeric(precision=10, scale=2))
    szn_rcv_td = db.Column(db.Numeric(precision=10, scale=2))
    token = db.Column(db.String, nullable=False)

    def __init__(self, player_name, position, team, total_standard, total_ppr, total_hppr, szn_pass_y, szn_rush_y, szn_rcv_y, szn_pass_td, szn_rush_td, szn_rcv_td, token, starting=False):
        self.id = self.set_id()
        self.player_name = player_name
        self.position = position
        self.team = team
        self.total_standard = total_standard
        self.total_ppr = total_ppr
        self.total_hppr = total_hppr
        self.szn_pass_y = szn_pass_y
        self.szn_rush_y = szn_rush_y
        self.szn_rcv_y = szn_rcv_y
        self.szn_pass_td = szn_pass_td
        self.szn_rush_td = szn_rush_td
        self.szn_rcv_td = szn_rcv_td
        self.starting = starting
        self.token = token

    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f"{self.player_name} has been added to your roster."

class PlayerSchema(marsh.Schema):
    class Meta:
        fields = ['id', 'starting', 'player_name', 'position', 'team', 'total_standard', 'total_ppr', 'total_hppr', 'szn_pass_y', 'szn_rush_y', 'szn_rcv_y', 'szn_pass_td', 'szn_rush_td', 'szn_rcv_td']

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


