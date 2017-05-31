#1.完成基本类
#2.完成handler
#3.检查冲突和json
#4.前端

from flask import Flask,request,render_template
import pymysql
import json
import logging

app=Flask(__name__)
res=''
#----------------------------------------
#Maybe this global attr can be solved by Class functions (Maybe in Handler class?)
#Base Classes===========================================
#为了更便捷地操作和提取属性，对当前选中的数据库和表建立模型
#每次更改选项会更新对象,对象中不包括数据的细节，只有基本属性
#***这几个类是嵌套的 Handler->sql->databases->tables***
#数据细节由cursor.fetchall()确定 加上对象中的列名，产生较完整的Json格式，便于js读取
class sql(object,user):
	def __init__(self):
		#init------------------直接对用户建立对象，避免冲突
		try:
		#登录界面之后选择登入的dbs，之后更改用use语句就可以了
			conn=pymysql.connect(user='root',password='')
		except pymysql.err.OperationalError as e:
			print('Error:',e.args)
			logging.exception(e)
		else:
			cursor=conn.cursor()
	
		print('start service')
		self.__user=user
		self.__dbs_num=cursor.execute('show databases')
		self.__dbs_name=cursor.fetchall()
		self.dbs_now=databases()
	
	def flush():
		pass
	
	def change_database(dbsname):
		pass
		
class databases(object,dbsname):
	def __init__(self,dbsname):
		self.__dbs_name=dbsname
		self.__table_num=cursor.execute('show tables')
		self.__table_name=cursor.fetchall()
		self.table_now=
		
	def flush():
		pass
	
	def change_table(tablename,dbsname):
		pass
		
class tables(object,tablename,dbsname):
	def __init__(self,tablename):
		self.__parent_dbs=dbsname				#下面函数是通用的，要传入数据库名和表名
		self.__table_name=tablename
		self.__colomn_num=cursor.execute('select column_name,data_type from information_schema.columns where table_name="%s"' % __tablename)
		self.__colomn_info=cursor.fetchall()	#colomn name&types
			
	def flush():
		pass
		
	def get_types():
		pass
	
	def get_names():
		pass

#sql_now=sql()
#dbs_now=databases(dbsname)
#tab_now=tables(tabname)

#Handler Functions======================================
#每种行为在前端js都有对应的信息包
#修改的都是当前选中的表，所以传入表对象
#产生信息：列名及对应数据类型（列数）
#以下所有函数的测试部分要换成动态构造

class Sql_Handler(object,user,grantlist)：	#准备把这些函数都扔到Handler类里，并为其加一些便利的参数->比如用户和权限之类的
	def __init__():							#从权限表里（不是sql里的权限）找用户名对应权限
		self.res=''
		self.__user=user
		self.__grant=grantlist[user]
		self.mainSql=sql(self.__user)
		self.functions={'swi':switching,
						'upd':update_info,
						'cmt':commit,
						'ser':search,
						'ins':insert,
						'isr':insert_rows,
						'del':delete,
						'adc':add_col
						}
						
	def get_name():				#返回包含当前库名和表名的tuple
		name=(self.mainSql.dbs_now.__dbs_name,self.mainSql.dbs_now.table_now.table_name)
		return name

	def switching(msg):  		#记得同时更新insert的框框
		pass
	
	def update_info(msg):		#msg里 有分改dbs和改table 两种参数
		pass
	
	def commit(msg):
		global res
		print('Commiting...')
		conn.commit()
		res=dict(type=2,response='Commited!')
		return res
	
#Elem op (need tab info)
	def search(msg,tab=get_name()): 	#Search的msg需要两个参数了，列名和值（小改）
		name=msg['request']
		print('Searching:',name)
		patten='ORDER: SELECT * FROM %s.%s WHERE name="%s"' % (tab[0],tab[1],name)
		print(patten)
		cursor.execute(patten)
		re=cursor.fetchall()
		length=len(re)
		
		res=dict(type=1,length=length,response=re)
		return res
		#print(res)

	def insert(msg,tab=get_tab_now()):    #从tab获取列数，自动构造exec语句（估计要大改），而且要向web页面返回相应结构 动态构造输入框
		#如果需要变长参数，可以用构造函数
		print('Inserting:',msg)				 #***这个变长一定要改，可以用字符串拼接插入
		patten='INSERT INTO %s.%s VALUES(%d,%d,%d)' % (tab[0],tab[1],msg['request'][0],msg['request'][1],msg['request'][2])
		print(patten)
		cursor.execute(patten)
		
		res=dict(type=2,response='succeed')
		return res

	def insert_rows(msg,tab):#msg中有加几行，什么内容
		pass
	
	def delete(msg,tab=get_tab_now()):	#同样地，双参数
		print('Deleting:',msg)
		patten='DELETE FROM %s,%s WHERE name="%s"' % (tab[0],tab[1],msg['request'])
		print(patten)
		cursor.execute(patten)
		
		res=dict(type=2,response='succeed')
		return res
	
	def add_col(msg,tab=get_tab_now()): #加一列 msg:列名
		pass


#以下的函数基本定型
#===========================================这是个信息传接函数 负责：↓
@app.ronte('/login',methods=['POST'])
def login():
	msg=msg=request.form['message']			#应该包含user passwd
	
@app.route('/op',methods=['POST'])
def main_dbs_op():							#接收json，选择函数，错误处理，返回json								
	msg=request.form['message']				#json用的dict由所选函数或错误块自行构造
	#print(msg)								#在修改功能时，这一段受影响较小，只需要向handler中添加函数即可
	msg=json.loads(msg)						#选择函数的信息在request包里
	print(msg)
	
	try:	#***要想办法解决一下参数长度不一样的问题，有些函数要传入table对象
			#其实只传入一个参数就够了
		res=Handler.functions[msg['type']](msg)		#type:Succeed 的 res 组装在集成操作函数内进行
	except pymysql.err.InternalError as e:			#type:Error 的 res 由错误处理进行 *所有错误都在外部抓取，不在具体函数内进行
		res='%s %s'%e.args							#两者并不冲突 ,因为一旦execute失败 就会跳过之后的dict组装
		res=dict(type=2,response=res)
	except pymysql.err.ProgrammingError as e:
		res='%s %s'%e.args
		res=dict(type=2,response=res)
	finally:
		res=json.dumps(res)							#在最后统一打包json格式
		print("[RES:%s]"%res)
		return res,200,{'Access-Control-Allow-Origin':'*'}

@app.route('/',methods=['GET'])	
def search_main():
	return render_template('simple_ajax.html'),200,{'Access-Control-Allow-Origin':'*'}
	
if __name__=='__main__':
    app.run(debug=True,port=8820)