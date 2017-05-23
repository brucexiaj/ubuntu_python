#coding=utf-8

#定义变量
a=1;
a=100-a;
print a;

#组合运算符号
a-=1;
print a;

#定义函数
def myPrint(s):
    print s
    return

#调用函数
myPrint("下军");

#定义带返回值的函数
def function1(i):
    t=i+1
    return t
args=100;
print "结果是:"+str(function1(args));

#字符串转义
news="she said:I\'m a student";
print(news);
print("打印特殊符号："+"\\");
print("\'");

#如果print后面是逗号，打印的结果不换行
print("我是打印"),
print("函数");

#格式化打印
my_int=1;
my_float=2;
my_string="ni cai";
print("格式化打印：%d;%f;%s"%(my_int,my_float,my_string));

#获取用户输入的字符串,可以用input或者raw_input函数
userinput=raw_input("请输入字符串：");
print("你输入的是："+userinput);
userInput=input("请输入数字：");
intValue=int(userInput)*2;
print("你输入的数字的两倍是:"),
print(intValue);

#使用已有的模块
import math;
print(math.sqrt(16));

#使用自己的模块
import myModule
myModule.myModuleFunction(12)

#！！！！下面三条很重要，表明了值传递和引用传递的区别！！！！

#python中实际参数的值在函数中是不会改变的,大部分情况下是这样
def changeArgs(t):
    t=13
    return None
realArgs=11
changeArgs(realArgs)
print("当前realArgs的值是"+str(realArgs))

#但是列表等类型实际参数的值在函数中是可以改变的
def changeListArgs(listArgs):
    for i in range(len(listArgs)):
        listArgs[i]+=1
    return None
realList=[1,2,3,4,5]
changeListArgs(realList)
print("调用了函数之后的列表是：")
print(realList)#从打印的结果来看，列表中的值都改变了

#函数的使用
#如果是自己建的类，而不是基本类，那么等号传递过去的只是引用！！！
#所以student2的age也发生了改变
class Student:
    name="default"
    age=0
    def __init__(self,name,age):#左右都是两个下划线!!!
        self.name=name
        self.age=int(age)
    def changeAge(self):
        self.age+=1
student1=Student('xiajun',22)
student2=student1
student2.changeAge()
print student2.age
print student1.age

#try-catch异常处理
listtry=[1,2,3,4,5]
try:
    print listtry[5]
except IndexError:
    print "数组越界异常"
except ZeroDivisionError:
    print "除数为0异常"
except AttributeError:
    print "调用不存在方法引发的异常"
except:
    print "未知类型的异常"
else:
    print "未捕获异常"

#多重异常
listMulti=[1,2,3]
try:
    try:
        zero=listMulti[1]/0
    except IndexError:
        print "内层的数组越界异常"
except ZeroDivisionError:
    print "外层捕获到了除数为0的异常"
else:
    print "没有异常"

#使用assert引发异常
assertEx=[]
try:
    assert len(assertEx)#测试条件为假引发异常
except:
    print "Assert发现异常"
else:
    print "没有异常"

#自定义异常类
class myException(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data
try:
    raise myException,"发现了自定义异常"
except myException,data:
    print data
else:
    print "没发现自定义异常"

#列表的使用
listDemo=[1,2,3,4,5]
print "列表长度"+str(len(listDemo))
print listDemo[-1]
print "子列表是："
childList=listDemo[2:-1]
for element in childList:
    print element
listDemo.reverse()
print "倒转后的列表是："
for newEle in listDemo:
    print newEle
listDemo.append(6)
listDemo.append(5)
fre=listDemo.count(5)
print "次数:",
print fre
secondList=[7,8,[9,10]]
listDemo.extend(secondList)
print "追加后的列表是:",
for element in listDemo:
    print element,#逗号表示打印不换行

#字典的使用
my_dict={'name':'xiajun','age':22,"sex":'boy',"like":'girl'}
allKeys=my_dict.keys()
print "\n所有的键是：",
for key in allKeys:
    print key,
print "\nlike:",
print my_dict.get('like')
my_dict.update({'age':21})
print "age:",
print my_dict['age']
print my_dict.has_key('sex')


