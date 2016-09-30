#!/usr/bin/python3
# -*-coding:utf-8-*-

import sqlite3

# 链接数据库
connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel

# """
# 新建数据库 coachdata.sqlite
# """
# import sqlite3
#
# connection=sqlite3.connect("coachdata.sqlite")
# cursor = connection.cursor()
# cursor.execute("""
# CREATE TABLE athletes(
# id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL ,
# name TEXT NOT NULL ,
# dob DATE NOT NULL
# )
# """)
# cursor.execute("""
# CREATE TABLE timing_data(
# athlete_id INTEGER NOT NULL ,
# value TEXT NOT NULL ,
# FOREIGN KEY (athlete_id) REFERENCES athletes
# )
# """)
# connection.commit()

# 从现有模型获取数据
data_file = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_file)

# “腌制”数据后得到名字和出生日期
for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob

    # 使用INDERT 语句向表athletes中添加数据行
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)", (name, dob))
    # 使修改永久保存
    connection.commit()

# 关闭链接
connection.close()
