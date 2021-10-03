import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setting import app

db = SQLAlchemy(app)


class Coffee(db.Model):
    __tablename__ = "coffee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    origin = db.Column(db.String(80), nullable=False)
    usage = db.Column(db.String(80), nullable=False)
    side = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "origin": self.origin,
            "usage": self.usage,
            "side": self.side,
        }

    def add_coffee(_name, _origin, _usage, _side):
        new_coffee = Coffee(name=_name, origin=_origin, usage=_usage, side=_side)
        db.session.add(new_coffee)
        db.session.commit()

    def get_all():
        return [Coffee.json(coffee) for coffee in Coffee.query.all()]

    # mencari id
    def get_coffee(_id):
        return Coffee.json(Coffee.query.filter_by(id=_id).first())

    def delete_coffee(_id):
        Coffee.query.filter_by(id=_id).delete()
        db.session.commit()

    def update_coffeeName(_id, _name):
        coffee_to_update = Coffee.query.filter_by(id=_id).first()
        coffee_to_update.name = _name
        db.session.commit()

    def update_coffeeOrigin(_id, _origin):
        coffee_to_update = Coffee.query.filter_by(id=_id).first()
        coffee_to_update.origin = _origin
        db.session.commit()

    def update_coffeeUsage(_id, _usage):
        coffee_to_update = Coffee.query.filter_by(id=_id).first()
        coffee_to_update.usage = _usage
        db.session.commit()

    def update_coffeeSide(_id, _side):
        coffee_to_update = Coffee.query.filter_by(id=_id).first()
        coffee_to_update.side = _side
        db.session.commit()

    def replace_coffee(_id, _name, _origin, _usage, _side):
        coffee_to_update = Coffee.query.filter_by(id=_id).first()
        coffee_to_update.name = _name
        coffee_to_update.origin = _origin
        coffee_to_update.usage = _usage
        coffee_to_update.side = _side
        db.session.commit()

    def __repr__(self):
        coffee_object = {
            "id": self.id,
            "name": self.name,
            "origin": self.origin,
            "usage": self.usage,
            "side": self.side,
        }
        return json.dumps(coffee_object)
