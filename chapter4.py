# -*-coding:utf8-*-
# man = []
# other = []
# try:
#     data = open('sketch.txt')
#     for each_line in data:
#         try:
#             (role, line_spoken) = each_line.split(":", 1)
#             line_spoken = line_spoken.strip()
#             if role == 'Man':
#                 man.append(line_spoken)
#             elif role == 'Other Man':
#                 other.append(line_spoken)
#         except:
#             pass
#     data.close()
# except IOError:
#     print ('The datafile is missing')
#
# print (man)
# print (other)



# man = []
# other = []
#
# try:
#     data = open('sketch.txt')
#     for each_line in data:
#         try:
#             (role, line_spoken) = each_line.split(':', 1)
#             line_spoken = line_spoken.strip()
#             if role == 'Man':
#                 man.append(line_spoken)
#             elif role == 'Other Man':
#                 other.append(line_spoken)
#         except:
#             pass
#     data.close()
# except IOError:
#     print ('The datafile is missing')
#
# try:
#     man_file = open('man_data.txt', 'w').writelines(man)
#     other_file = open('other_data.txt', 'w').writelines(other)
# except IOError:
#     print('file error')



# try:
#     data = open('its.txt')
#     print(data.readline())
# except IOError as err:
#     print ('File error:' + str(err))
# finally:
#     if 'data' in locals():
#         data.close()



# man = []
# other = []
#
# try:
#     data = open('sketch.txt')
#     for each_line in data:
#         try:
#             (role, line_spoken) = each_line.split(':', 1)
#             line_spoken = line_spoken.strip()
#             if role == 'Man':
#                 man.append(line_spoken)
#             elif role == 'Other Man':
#                 other.append(line_spoken)
#         except:
#             pass
#     data.close()
# except IOError:
#     print ('The datafile is missing')
#
# try:
#     with open('man_data.txt', 'w') as man_file:
#         for item in man:
#             man_file.writelines(item)
#             man_file.write("\n")
#             # man_file.write(repr(man)+"\t")
#             # man_file.writelines(man)#写入文件后不保持list格式
#     with open('other_data.txt', 'w') as other_file:
#         for item in other:
#             other_file.writelines(item)
#             other_file.write("\n")
# except IOError as err:
#     print ('FIle error:' + str(err))


# f=file("hello.txt","w+")
# li=["hello world\n","hello china\n"]
# f.writelines(li)
# f.close()


# import sys
#
# def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item,indent,level+1,fh)
#         else:
#             if indent:
#                 for tab_stop in range(level):
#                     print ("\t",file = fh)
#             print (each_item,file+fh)


# 腌制数据
import struct
import pickle

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except:
            pass
    data.close()
except IOError:
    print ('The datafile is missing')

try:
    with open('man_data2.txt', "wb") as man_file:
        pickle.dump(man, man_file)#写入
        # for item in man:
        #     man_file.write(item)
        #     man_file.write("\n")

        man_file.close()
        #     # man_file.write(repr(man)+"\t")
        #     # man_file.writelines(man)#写入文件后不保持list格式
    with open('other_data2.txt', "wb") as other_file:
        for item in other:
            other_file.write(item)
            other_file.write("\n")
        other_file.close()
    with open('man_data2.txt', "rb") as man_file:
        data1 = pickle.load(man_file)#读出
        print data1
except IOError as err:
    print ('FIle error:' + str(err))
