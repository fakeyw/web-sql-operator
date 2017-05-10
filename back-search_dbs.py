'''
Back Part
Simple template of py-sql-easyOp 
With no filiter
only for personal use
From:fakeyw(10miric)
Email:main@fakeyw.top
=====================
Waiting for Update->

1.Better
Divide the functions is Foolish
So i will restore them after
toooooooo much repeat!!!!

2.Stronger
*Basic Functions:
Change dbs
Change table
Creat dbs
Creat table
Change user
User login

*Advanced Functions:
Concise code structure							√
Read all dbs&tables and given choices
Filiter
User grant management
Muti insert


3.Easier
Auto commit choice as box
Front part UI
Dynamic table display

=======================================================
Standered response JSON:
{
	"type":(1,2,...)		//1:tableinfo 2:status info
   ("length":(1,2,...)) 	//for select
	"response": //for select
		[
			[a,b,c],
			[d,e,f],
			...
		]
		or
		"ERROR:......"  	//for all error
		or
		"Succeed!..."			//for insert/delete/commit
}
========================================================
'''
#以后东西多了可以给改成面向对象版？
from flask import Flask,request,render_template
import pymysql
import json
import logging

try:
	conn=pymysql.connect(user='root',password='',database='try')
except pymysql.err.OperationalError as e:
	print('Error:',e.args)
	logging.exception(e)
else:
	cursor=conn.cursor()

app=Flask(__name__)
print('start service')

res=''
#Maybe this global attr can be solved by Class functions
#Base Classes===========================================
#为了更便捷地操作和提取属性，对当前选中的数据库和表建立模型
#每次更改选项会更新对象,对象中不包括数据的细节，只有基本属性
#数据细节由cursor.fetchall()确定 加上对象中的列名，产生较完整的Json格式，便于js读取
class dbs_now():
	def __init__(self):
		
		
		
		
		
class tab_now():

#Handler Functions======================================
#修改的都是当前选中的表，所以传入表对象
#产生信息：列名及对应数据类型（列数）
def search(msg,tab):
	global res
	name=msg['request']
	print('Searching:',name)
	print('ORDER: SELECT * FROM new WHERE name=%s' % name)
	cursor.execute('SELECT * FROM new WHERE name=%s' % name) # name=1 or 1=1 XXX msg is number
	re=cursor.fetchall()
	length=len(re)
	res=dict(type=1,length=length,response=re)
	#print(res)

def insert(msg,tab):
	global res
	#如果需要变长参数，可以用构造函数
	print('Inserting:',msg)
	patten='INSERT INTO new VALUES(%d,%d,%d)' % (msg['request'][0],msg['request'][1],msg['request'][2])
	print(patten)
	cursor.execute(patten)
	res=dict(type=2,response='succeed')

def insert_cons(length):
	pass
	
def delete(msg,tab):
	global res
	print('Deleting:',msg)
	patten='DELETE FROM new WHERE name=%s' % msg['request']
	print(patten)
	cursor.execute(patten)
	res=dict(type=2,response='succeed')

def commit(msg,tab):
	global res
	print('Commiting...')
	conn.commit()
	res=dict(type=2,response='Commited!')

def switching(msg,tab):
	
	
	
Handler=dict(ist=insert,ser=search,dele=delete,cmt=commit)
#======================================================

@app.route('/op',methods=['POST'])
def main_dbs_op():
	global res
	msg=request.form['message']
	#print(msg)
	msg=json.loads(msg)
	print(msg)
	
	try:
		Handler[msg['type']](msg) 			#type:Succeed 的 res 组装在集成操作函数内进行
	except pymysql.err.InternalError as e:	#type:Error 的 res 由错误处理进行
		res='%s %s'%e.args					#两者并不冲突 ,因为一旦execute失败 就会跳过之后的组装
		res=dict(type=2,response=res)
	except pymysql.err.ProgrammingError as e:
		res='%s %s'%e.args
		res=dict(type=2,response=res)
	finally:
		res=json.dumps(res)					#在最后打包json格式
		print("!RES!:")
		print(res)
		return res,200,{'Access-Control-Allow-Origin':'*'}
		
@app.route('/',methods=['GET'])	
def search_main():
	return render_template('ajax2.html'),200,{'Access-Control-Allow-Origin':'*'}
	
if __name__=='__main__':
    app.run(debug=True,port=8820)