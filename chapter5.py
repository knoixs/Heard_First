# -*-coding:utf-8-*-
"""
第五章处理数据
"""


# import os
# print os.getcwd()

# with open('hfpy_ch5_data/james.txt', 'r') as jaf:
#     data = jaf.readline()
# james = data.strip().split(',')
# # print james
#
# with open('hfpy_ch5_data/julie.txt','r') as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# # print julie
#
# with open('hfpy_ch5_data/mikey.txt','r') as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# # print mikey
#
# with open('hfpy_ch5_data/sarah.txt','r') as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')
# # print sarah
#
# def sanitize(item):
#     if '-' in item:
#         split_item = '-'
#     elif ':' in item:
#         split_item = ':'
#     else:
#         return item
#     (mit, sec) = item.split(split_item)
#     return mit+'.'+sec
#
# print sorted(set([sanitize(item)for item in james]))[0:3]
# print sorted(set([sanitize(item)for item in julie]))[]
# print sorted([sanitize(item)for item in mikey])
# print sorted([sanitize(item)for item in sarah])
#
# james2=[]
# for item in clean_james:
#     if item not in james2:
#         james2.append(item)
# print james2[0:3]
#
# sorted(reverse=False)


def get_coach_data(filename):
    try:
        with open('hfpy_ch5_data/' + filename, 'r') as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as err:
        print ('File error' + str(err))
        return None


james = get_coach_data('james.txt')
sarah = get_coach_data('sarah.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')


def sanitize(item):
    if '-' in item:
        splt_item = '-'
    elif ':' in item:
        splt_item = ':'
    else:
        return item
    (mit, sec) = item.split(splt_item)
    return mit + '.' + sec


print sorted(set([sanitize(item) for item in james]))[0:3]
print sorted(set([sanitize(item) for item in julie]))[0:3]
print sorted(set([sanitize(item) for item in mikey]))[0:3]
print sorted(set([sanitize(item) for item in sarah]))[0:3]
