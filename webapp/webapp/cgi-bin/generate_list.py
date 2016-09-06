#!/usr/bin/python3
# -*-coding:utf-8-*-
import athletemodel
import yate
import sys
# 利用“glob”模块可以向操作系统查询一个文件列表
import glob

# print sys.path
data_files = glob.glob("/home/knoix/PycharmProjects/Heard_First/webapp/webapp/data/*.txt")
athletes = athletemodel.put_to_store(data_files)
# 总是从一个Content-type行开始
print (yate.start_response())
print (yate.include_header("Coac Kelly's List of Athletes"))
print (yate.start_form("generate_timing_data.py"))
print (yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print (yate.radio_button("which_athlete", athletes[each_athlete].name))
print (yate.end_form("Select"))

print (yate.include_footer({"Home": "/index.html"}))
