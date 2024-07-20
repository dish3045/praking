from flask import Flask,render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy.orm import backref
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dishakowshik@localhost/parking'
db=SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.String(20),primary_key=True)
    first_name=db.Column(db.String(20))
    last_name=db.Column(db.String(20))
    email=db.Column(db.String(20))
    password=db.Column(db.String(20))
    number_plate=db.Column(db.String(10))
    isadmin=db.Column(db.Integer())

class Location(db.Model):
    __tablename__='location'
    parkinglot_id=db.Column(db.String(20),primary_key=True)
    parkinglot_name=db.Column(db.String(20))
    latitude=db.Column(db.String(20))
    longitude=db.Column(db.String(20))
    total_spots=db.Column(db.Integer())
    empty_spots=db.Column(db.Integer())
    cost_perhour=db.Column(db.Integer())

class Billing(db.Model):
    __tablename__='billing'
    user_id=db.Column(db.String(20),db.ForeignKey('user.user_id'))
    user=db.relationship("User", backref=backref("user", uselist=False))
    parkinglot_id=db.Column(db.String(20),db.ForeignKey('location.parkinglot_id'))
    location=db.relationship("Location", backref=backref("location", uselist=False))
    bill_id  = db.Column(db.String(20),primary_key=True)

    checkin_time=db.Column(db.Time)
    checkout_time=db.Column(db.Time)
    total_cost=db.Column(db.Integer())

class Parking_slot(db.Model):
    __tablename__='parking_slot'
    parkingslot_id=db.Column(db.String(20),primary_key=True)
    parkinglot_id=db.Column(db.String(20),db.ForeignKey('location.parkinglot_id'))
    location=db.relationship("Location", backref=backref("location", uselist=False))

    floor_num=db.Column(db.Integer())
    IsEmpty=db.Column(db.Integer())

class MonthlyPass(db.Model):
    __tablename__='monthlypass'
    pass_id=db.Column(db.String(20),primary_key=True)
    user_id=db.Column(db.String(20),db.ForeignKey('user.user_id'))
    user=db.relationship("User", backref=backref("user", uselist=False))

    pass_indate=db.Column(db.Date)
    pass_expdate=db.Column(db.Date)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("")

if __name__ == "__main__":
   app.run(debug=True) 