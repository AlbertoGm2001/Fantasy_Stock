import pandas as pd 
from config import db,app



    
    

class User(db.Model):
    #players-bids will be a dictionary with key a player_id and value a bid

    user_id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(80),nullable=False)
    players_bids=db.Column(db.JSON)
    
   

    def to_json(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'players_bids': self.players_bids,
        }   

    def __repr__(self):
        return f'<User {self.user_id}>'

class Player(db.Model):
    player_id=db.Column(db.Integer,primary_key=True)
    player_name=db.Column(db.String(80),nullable=False)
    team=db.Column(db.String(80),nullable=False)
    position=db.Column(db.String(80),nullable=False)
    total_bids=db.Column(db.Integer,nullable=False)
    value=db.Column(db.Float,nullable=False)
    prev_scores=db.Column(db.JSON)

    


    def to_json(self):
        return {
            'player_id': self.player_id,
            'player_name': self.player_name,
            'team': self.team,
            'position': self.position,
            'total_bids': self.total_bids,
            'value': self.value,
            'prev_scores': self.prev_scores,
        }

    def __repr__(self):
        return f'<Player {self.player_id}>'




