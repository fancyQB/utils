import random
import numpy as np
from collections import Counter


#一行代码实现1-100之间的和


def thesum():
	print(sum(range(1,101)))

#如何在一个函数内部修改全局变量
a = 100
def fun():

	global a 
	a= 10
	print(a)

#列出5个python标准库
# os sys re math datetime

#字典如何删除键和合并两个字典
def de():
	A = dict(a=1, b=2)
	del A['a']
	print(A)
	B = {'name':"zuo", 'age':'18'}
	B.update(A)
	print(B)


#列表去重
def ss():
	lis = ['a', 'b', 'a', 'c']
	lis1 = set(lis)
	print(lis1)

# init方法初始化后会自动被调用,可接收参数
class Bike: 

	def __init__(self, newWheelNum, newCololr):
		self.wheelNum = newWheelNum
		self.Cololr = newCololr

	def price(self):

		print(200) 

class A(object):
	def __init__(self):
		print('init方法', self)

	def __new__(cls):
		print('cls的id', id(cls))
		print('new方法', object.__new__(cls))
		#return object.__new__(cls)
		return super().__new__(cls)
#列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25] map(函数, 列表)
def get_result():
	list1 = [1, 2, 3, 4, 5]
	def fn(x):
		return x**2
	res = map(fn, list1)
	res = [i for i in res if i>10]
	print(res)
#随机生成整数,随机小数,0-1之间的小数方法
def get_rand():
	result = random.randint(10,20)
	res = np.random.randn(5)
	ret = random.random()
	print('正整数: ',result )
	print('小数', res)
	print('0-1小数', ret)
#去重,排序
def Deduplication():
	s = "ajldjlajfdljfddd"
	s = set(s)
	s= list(s)
	s.sort()
	res = ''.join(s)
	print(s)
#lambda函数
def get_la():
	
	sum = lambda a,b:a*b
	print(sum(3,4))

def order():

	dic = {'name': 'zuoqiang', 'age': '25', 'city': '深圳', 'tel': '15926440508'}
	lis = sorted(dic.items(), key=lambda i:i[0], reverse=False)
	print(dict(lis))
def ex25():

	a= "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
	b=''
	for i in a :
		if i!=';':
			b +=i
	res = Counter(b)
	print(res)

def ex26():
	import re

	a = 'not 404 found 张三 99 深圳'
	list1 = a.split(' ')
	print(list1)
	res = re.findall('\d+|[a-zA-Z]+', a)

	for i in res:
		if i in list1:
			list1.remove(i)
	print(list1)
	new_str = ' '.join(list1)
	print(new_str)


def ex27():
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	def fn(x):
		return x%2==1
	new_list = filter(fn, a)
	new_list = [i for i in new_list]
	print(new_list)

def ex28():
	a = [1,2,3,4,5,6,7,8,9,10]
	a = [i for i in a if i%2==1]
	print(a)	

def ex30():
	a = (1,)
	b = (1)
	c = ('1')
	print (type(a),type(b),type(c))

def ex31():
	l1 = [1, 5, 7, 9]
	l2 = [2, 2, 6, 8]
	l1.extend(l2)
	print(l1)
	l1.sort(reverse=False)
	print(l1)
'''
python删除文件的方法 和linux删除文件的方法

python: os.remove(文件名字)
linux : rm 文件名
'''
def ex33():
	
	import datetime
	warning_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+' 星期:'+str(datetime.datetime.now().isoweekday())
	print(warning_time)

def ex36():
	try:
		for i in range(5):
			if i >3:
				raise Exception('数字大于2')
	except Exception as ret:
		print(ret)

def ex39():

	a = [[1, 2], [3, 4], [5, 6]]
	x = [j for i in a for j in i ]
	print(x)
	import numpy as np
	b = np.array(a).flatten().tolist()
	print(b)

'''
@左:冒泡
def ex40():

	list1 = [2,3,7,5,9,6]
	for j in range(len(list1))[::-1]:
		
		for i  in range(j):
			if list1[i]>list1[i+1]:
				swap_num = list1[i]
				list1[i] = list1[i+1]
				list1[i+1] = swap_num
	print(list1)

'''
#顺序
class ex40(object):
	list1 = [2,3,4,5,9,6]
	new_list = []
	def get_min(self, list, new_list):
		min_num = min(list)
		list.remove(min_num)
		new_list.append(min_num)
		if len(list) > 0:
			self.get_min(list, new_list)
		return new_list
#单例模式
class Single:

	__instance = None

	def __new__(cls, *args, **kwargs):

		if cls.__instance is None:
			cls.__instance = object.__new__(cls, *args, *kwargs)
		return cls.__instance
	def __init__(self):
		pass

#函数装饰器实现单例
def single(cls):

	__instance = {}

	def inner():
		if cls not in __instance:
			__instance[cls] = cls()
		return __instance[cls]
	return inner
@single
class A:

	def __init__(self):
		pass
	
#类装饰器实现单例
class Singleton:

	def __init__(self, cls):

		self._cls = cls
		self._instance = {}

	def __call__(self):

		if self._cls not in self._instance:

			self._instance[self._cls] = self._cls()
		return self._instance[self._cls]

@Singleton
class B(object):
	"""docstring for B"""
	def __init__(self):
		pass
def ex54():

	a = '%.03f'%1.3335
	print(a, type(a))
	b = round(float(a), 1)
	print(b)
	b = round(float(a), 2)
	print(b)

def ex55(k, v, dic={}):

	dic[k] = v
	print(dic)

def ex84(num)
	
	if num>0:

		res = num + ex84(num-1)
	else:
		return res



if __name__ == '__main__':
	
	ex55('one', 1)
	ex55('two', 2)
	ex55('three', 3, {})