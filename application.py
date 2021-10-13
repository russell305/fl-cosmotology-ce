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
db = scoped_session(sessionmaker(bind=engine)) # for individual sessionss

# utils.recent_certificates()
# utils.recent_certificates_csv()

# db.execute("CREATE TABLE fl_life_health_agent_1(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL UNIQUE,email VARCHAR NOT NULL, password VARCHAR NOT NULL, address VARCHAR NOT NULL,first VARCHAR NOT NULL,last VARCHAR NOT NULL,license_no VARCHAR NOT NULL,license_state VARCHAR NOT NULL, maiden VARCHAR NOT NULL, color VARCHAR NOT NULL, ethics_paid Boolean, ethics_course  Boolean, ethics_score_date VARCHAR, course_2_paid Boolean, course_2_complete Boolean, course_2_score_date VARCHAR,  course_3_paid Boolean, course_3_complete Boolean, course_3_score_date VARCHAR, course_4_paid Boolean, course_4_complete Boolean, course_4_score_date VARCHAR)")
# db.commit()

#adds comma
# df3.to_csv('lh-group-1.csv', index=False, header=False, line_terminator=',\n')



@app.route("/", methods = ["GET", "POST"])
def index():
	session['admin'] = False #causing errors timing out
	# return "hihihihibnbnxxxxxx"
	return render_template("main_page.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
	answers_correct = 0
	result_1 = request.form.get("1", "")
	result_2 = request.form.get("2", "")
	result_3 = request.form.get("3", "")
	result_4 = request.form.get("4", "")
	result_5 = request.form.get("5", "")
	result_6 = request.form.get("6", "")
	result_7 = request.form.get("7", "")
	result_8 = request.form.get("8", "")
	result_9 = request.form.get("9", "")
	result_10 = request.form.get("10", "")
	result_11 = request.form.get("11", "")
	result_12 = request.form.get("12", "")
	result_13 = request.form.get("13", "")
	result_14 = request.form.get("14", "")
	result_15 = request.form.get("15", "")
	result_16 = request.form.get("16", "")
	result_17 = request.form.get("17", "")
	result_18 = request.form.get("18", "")
	result_19 = request.form.get("19", "")
	result_20 = request.form.get("20", "")
	result_21 = request.form.get("21", "")
	result_22 = request.form.get("22", "")
	result_23 = request.form.get("23", "")
	result_24 = request.form.get("24", "")
	result_25 = request.form.get("25", "")
	result_26 = request.form.get("26", "")
	result_27 = request.form.get("27", "")
	result_28 = request.form.get("28", "")
	result_29 = request.form.get("29", "")
	result_30 = request.form.get("30", "")

	if result_1 == "c":
		answers_correct +=1
	if result_2 == "c":
		answers_correct +=1
	if result_3 == "c":
		answers_correct +=1
	if result_4 == "c":
		answers_correct +=1
	if result_5 == "c":
		answers_correct +=1
	if result_6 == "c":
		answers_correct +=1
	if result_7 == "c":
		answers_correct +=1
	if result_8 == "c":
		answers_correct +=1
	if result_9 == "c":
		answers_correct +=1
	if result_10 == "c":
		answers_correct +=1
	if result_11 == "c":
		answers_correct +=1
	if result_12 == "c":
		answers_correct +=1
	if result_13 == "c":
		answers_correct +=1
	if result_14 == "c":
		answers_correct +=1
	if result_15 == "c":
		answers_correct +=1
	if result_16 == "c":
		answers_correct +=1
	if result_17 == "c":
		answers_correct +=1
	if result_18 == "c":
		answers_correct +=1
	if result_19 == "c":
		answers_correct +=1
	if result_20 == "c":
		answers_correct +=1
	if result_21 == "c":
		answers_correct +=1
	if result_22 == "c":
		answers_correct +=1
	if result_23 == "c":
		answers_correct +=1
	if result_24 == "c":
		answers_correct +=1
	if result_25 == "c":
		answers_correct +=1
	if result_26 == "c":
		answers_correct +=1
	if result_27 == "c":
		answers_correct +=1
	if result_28 == "c":
		answers_correct +=1
	if result_29 == "c":
		answers_correct +=1
	if result_30 == "c":
		answers_correct +=1
	final_score = (answers_correct/30	) * 100
	print ('answers correct', answers_correct)
	print ('final score', final_score)

	if final_score <= 80:
		return render_template("final_pass.html", final_score = final_score)
	else:
		return render_template("final_fail.html", final_score = final_score)

@app.route('/complete_pay/', methods = ["GET","POST"])
def complete_pay():
	return 'ok here'
	first = request.form.get("first", "")
	last = request.form.get("last", "")
	license = request.form.get("license", "")
	course = request.form.get("course", "")
	rate = request.form.get("rate", "")
	expectation = request.form.get("expectation", "")
	objective = request.form.get("objective", "")
	comment = request.form.get("comment", "")

	print (first, last, license, course, rate, expectation, objective, comment)

	return render_template("complete_pay.html", first=first, last=last, license=license, course=course, rate=rate, expectation=expectation, objective=objective, comment=comment)

@app.route('/intro_cosmetologist/', methods = ["GET"])
def intro_cosmetologist():
	return render_template("intro_cosmetologist.html")


@app.route('/course_completion/', methods = ["GET"])
def course_completion():

	return render_template("course_completion.html")

@app.route('/cosmo_course/', methods = ["GET","POST"])
def cosmo_course():

	return render_template("cosmo_course.html")


@app.route('/faq/', methods = ["GET", "POST"])
def faq():
    # return "hihihihi"
	return render_template("faq.html")

@app.route('/contact/', methods = ["GET"])
def contact():
    # return "hihihihi"
	return render_template("contact.html")

@app.route('/sign_up_field/', methods = ["GET"])
def sign_up_field():
    # return "sign_up_field"
	return render_template("sign_up_field.html")

@app.route('/sign_in_main/', methods = ["GET","POST"])
def sign_in_main():
	return "sign_in"
	# return render_template("sign_in_main.html")

@app.route('/testimonials/', methods = ["GET"])
def testimonials():
    return "testimonials"
	# chapter = ia_courses.testimonials
	# return render_template("testimonials.html", chapter=chapter)

@app.route('/wrong_password/', methods = ["GET"])
def wrong_password():
	return "wrong_password"
	# return render_template("wrong_password.html")

@app.route('/forgot_password/', methods = ["GET","POST"])
def forgot_password():
	return "forgot_password"
	# return render_template("forgot_password.html")

@app.route('/unsubscribe/', methods = ["GET","POST"])
def unsubscribe():
	return "unsubscribe"
	# return render_template("unsubscribe.html")
