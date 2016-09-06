#!/usr/bin/python3
# -*-coding:utf-8-*-
import cgi
import athletemodel
import yate
import cgitb

cgitb.enable()

athletes = athletemodel.get_coach_data()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athele'].value

print (yate.start_response())
print (yate.include_header("Coach kelly's Timing Data"))
print (yate.header("Athlete:" + athlete_name + ",DOB:" + athletes[athlete_name].dob + "."))
print (yate.para("The top times for this athlete are:"))
print (yate.u_list(athletes[athlete_name].top3()))
print (yate.include_footer({"Home:": "/index.html", "Select another athlete": "generate.py"}))
