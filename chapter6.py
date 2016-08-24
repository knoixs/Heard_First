# -*-coding:utf-8-*-
"""
chater6,定制数据对象，打包代码和数据
"""


# # 将文件中的内容读出打列表中
# def get_cocah_data(filename):
#     try:
#         with open('hfpy_ch6_data/' + filename) as f:
#             data = f.readline()
#             return data.strip().split(',')
#     except IOError as err:
#         print 'file error' + str(err)
#         return None
#
#
# 将每个数据规范为'.'

def sanitize(item):
    if '-' in item:
        split_item = '-'
    elif ':' in item:
        split_item = ':'
    else:
        return item
    (mit, sec) = item.split(split_item)
    return mit + '.' + sec


#
#
# james = get_cocah_data('james2.txt')
# julie = get_cocah_data('julie2.txt')
# mikey = get_cocah_data('mikey2.txt')
# sarah = get_cocah_data('sarah2.txt')
#
# james_dict={}
# james_dict['name']=james.pop(0)
# james_dict['dob']=james.pop(0)
# james_dict['time']=james
#
# print (james_dict['name']+"'s fastest times are:"+str(sorted(set(sanitize(item)for item in james_dict['time']))))
#
# # # james_name,james_dob = james.pop(0),james.pop(0)
# # # james_name = james.pop(0)
# # james_name = james.pop(1)
# # # print james[0]
# # # print james_name
# # # print james
# # print sorted(set([sanitize(item) for item in james]))[0:3]
# #
# # plan = {'name':'james','dob':'d','sudu':2}
# # print plan
# # print plan['name']
# #
# # cless={}
# # cless['name']='julie'
# # cless['sudu']=None
# # print cless

# 讲文件中的数据读出，直接构建字典
def get_coach_data(filename):
    try:
        with open('hfpy_ch6_data/' + filename) as f:
            data = f.readline()
            temple = data.strip().split(',')
            return {'name': temple.pop(0),
                    'dob': temple.pop(0),
                    'time': str(sorted(set(sanitize(t) for t in temple))[0:3])}
    except IOError as err:
        print 'file error' + str(err)
        return None


# # 开始使用类
# class Athlete:
#     def __init__(self, value=0):
#         # The code to initialize a "Athlete" object.
#         self.thing = value
#
#     def how_big(self):
#         return len(self.thing)
#
#
# a = Athlete()  # Athlete().__init__(a) -->def __init__(self)
# d=Athlete("Holy girl")
# print d

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        # """
        #
        # :param a_name:
        # :param a_dob:
        # :param a_times:
        # :type a_name:str
        # :type a_dob:str
        # :type a_times:list
        # """

        self.name = a_name
        self.dob = a_dob
        self.times = a_times


sara = Athlete('Sara sweeney', '2002-6-17', ['2:58', '2.58', 1.56])
james = Athlete('James Jones')

print type(sara)
print sara.name, sara.dob
print james.name, james.dob, james.times
print sara