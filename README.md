# Heard_First笔记
heard_first_python
#在Pycharm的settings中设置project的interpreter为python3
#chapter6
类中的每个属性前面都必须有self，从而将数据与其对应的实例关联

#chapter7
Web服务器响应web请求的过程中，生成动态内容的过程得到标准化，成为网关接口（common Gateway Interface,CGI)。符合这个标准的程序成为CGI脚本。
pickle模块
```
piclke.dump(obj,file)
```

form_data=cgi.FieldStorage()#获取所有表单数据并放在一个字典中
athlete_name = form_data['which_athele'].value#从表单数据访问每一个指定的数据

@property————这是一个修饰符，可以使类方法表现得像是一个类属性

