
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#################################################
# Database Setup
#################################################

# engine = create_engine("sqlite:///db/NY.sqlite",connect_args={'check_same_thread': False}, echo=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/NY.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# Create our database model
class Leading_Death(db.Model):
    __tablename__ = 'Leading_Death'

    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.String)
    LeadingCause = db.Column(db.String)
    RaceEthnicity = db.Column(db.String)
    Deaths = db.Column(db.Integer)
    DeathRate = db.Column(db.Integer)
    AgeAdjustedDeathRate = db.Column(db.Integer)

    def __repr__(self):
        return '<Leading_Death %r>' % (self.LeadingCause)
#  Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

# Define what to do when a user hits the index route

@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Leading_Death).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names
    return jsonify(list(df.columns)[2:])

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)





@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    # 4. Define what to do when a user hits the /about route
    
@app.route("/Alldata")
def Alldata():
    """Return a list of all data"""
    # Query all record from database
    Leading_Death = Base.classes.Leading_Death
    results = db.session.query(Leading_Death)

    # Create a dictionary from the row data and append to a list of All_data
    All_data = []
    for Leading_Death in results:
        leadcause_dict = {}
        leadcause_dict["LeadingCause"] = Leading_Death.LeadingCause
        leadcause_dict["Year"] = Leading_Death.Year
        leadcause_dict["Sex"] = Leading_Death.Sex
        leadcause_dict["RaceEthnicity"] = Leading_Death.RaceEthnicity
        leadcause_dict["Deaths"] = Leading_Death.Deaths
        leadcause_dict["DeathRate"] = Leading_Death.DeathRate
        leadcause_dict["AgeAdjustedDeathRate"] = Leading_Death.AgeAdjustedDeathRate
        All_data.append(leadcause_dict)
      
    return jsonify(All_data)
    


if __name__ == "__main__":
    app.run(debug=True)
