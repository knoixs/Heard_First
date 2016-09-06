# -*-coding:utf-8-*-
"""
web开发
"""

import pickle
from chapter6 import AthleteList, get_coach_data


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
        # all_athletes['dob']=ath.dob
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print 'file error(put_to_store):' + str(err)
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print 'file error(get_from_store)' + str(err)
    return all_athletes


# print dir()
files = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
data = put_to_store(files)
# print data
for each_athlete in data:
    print data[each_athlete].name + ' ' + data[each_athlete].dob
    print data[each_athlete]

data_copy = get_from_store()
# print data_copy
# print type(data_copy)
# for item in data_copy:
#     print data_copy[item].name + ' ' + data_copy[item].dob
#     print data_copy[item]
