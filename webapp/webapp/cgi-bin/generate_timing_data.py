# -*-coding:utf-8-*-
#!/usr/bin/local/python3

# import cgi
# import athletemodel
# import yate
# import cgitb
# import json
# cgitb.enable()
#
#
# athletes = athletemodel.get_from_store()
#
# form_data = cgi.FieldStorage()
# athlete_name = form_data['which_athlete'].value
# print(yate.start_response())
# print(yate.include_header("Coach Kelly's Timing Data"))
# print(yate.header("Athlete: " + athlete_name + ", DOB: " +
#                       athletes[athlete_name].dob + "."))
# print(yate.para("The top times for this athlete are:"))
# print(yate.u_list(athletes[athlete_name].top3))
# print(yate.include_footer({"Home": "/index.html",
#                            "Select another athlete": "generate_list.py"}))


import cgi
# cgi跟踪模块
import cgitb
cgitb.enable()
import athletemodel, yate
athletes = athletemodel.get_from_store()
print (athletes)
print (cgi.FieldStorage())
#将所有表单数据放在一个字典中
form_data = cgi.FieldStorage()
# athlete_name = form_data['which_athlete'].value
athlete_name = form_data.getvalue('which_athlete')
print (form_data)

# 取出pickle数据


# 生成运动员时间显示页面
print(yate.start_response())
print(yate.include_header("时间数据信息"))
print(yate.header("运动员:" + athlete_name + ", 出生日期:" + athletes[athlete_name].dob + "."))
print(yate.para("最佳三次成绩为:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html", "其他成员数据": "generate_list.py"}))
