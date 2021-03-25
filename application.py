# export FLASK_APP=application.py
# set FLASK_APP=application.py
# top/mac bottom/windows
# set DATABASE_URL="postgres://bvyvdgxwtoixjr:fe8261a052ad6ba5997e288ef6d4a435b9f5d10be0e1dd8a7a452069f578dd97@ec2-52-204-20-42.compute-1.amazonaws.com:5432/ddju8atj54t423"


# put link on sign-in page to other courses...need to take more courses?

# fix title tags

#p tags need to have font size or make h-tag,for SEO. after all templates done.



#fix wrong password and cancel, there are duplicates

#adminer /

#test stripe black background

#heroku logs --tail
# heroku add ons
# move pa-image into folder do this last

from flask import Flask, render_template, request, session, jsonify, redirect, url_for# Import the class `Flask` from the `flask` module, written by someone else.
from flask_session import Session
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from pandas import read_csv
import json #for Python to Javascript
import requests #for JSON
import stripe
import hashlib #password
import re  #regex
import datetime
import math
import csv
import utils


app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# from flask_sslify import SSLify
# sslify = SSLify(app)

Session (app)
engine = create_engine("postgres://bvyvdgxwtoixjr:fe8261a052ad6ba5997e288ef6d4a435b9f5d10be0e1dd8a7a452069f578dd97@ec2-52-204-20-42.compute-1.amazonaws.com:5432/ddju8atj54t423")
#talk to datbase wiTh SQL. Object used to manage connections to database.
#Sending data to and from database.
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

#0275d8   primary  blue color

# utils.recent_certificates()
# utils.recent_certificates_csv()

# db.execute("CREATE TABLE fl_life_health_agent_1(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL UNIQUE,email VARCHAR NOT NULL, password VARCHAR NOT NULL, address VARCHAR NOT NULL,first VARCHAR NOT NULL,last VARCHAR NOT NULL,license_no VARCHAR NOT NULL,license_state VARCHAR NOT NULL, maiden VARCHAR NOT NULL, color VARCHAR NOT NULL, ethics_paid Boolean, ethics_course  Boolean, ethics_score_date VARCHAR, course_2_paid Boolean, course_2_complete Boolean, course_2_score_date VARCHAR,  course_3_paid Boolean, course_3_complete Boolean, course_3_score_date VARCHAR, course_4_paid Boolean, course_4_complete Boolean, course_4_score_date VARCHAR)")
# db.commit()
#relational database
# db.execute("CREATE TABLE ia_results_1(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL UNIQUE,name_id INTEGER REFERENCES fl_public_adjuster_1)")
# db.commit()
# user = db.execute("SELECT fl_public_adjuster_1.name FROM fl_public_adjuster_1 JOIN ia_results_1 ON fl_public_adjuster_1.id = ia_results_1.name_id WHERE ia_results_1.name = 'frank'  ").fetchall()
# now = datetime.datetime.now()
# print("today-date", now)


#adds comma
# df3.to_csv('lh-group-1.csv', index=False, header=False, line_terminator=',\n')



@app.route("/", methods = ["GET", "POST"])
def index():
    return "FLASK MINIMUM TEMPLATE"
	# session['admin'] = False #causing errors timing out
	# return render_template("main_page.html")
