'''
Back Part
Simple template of py-sql-easyOp 
With no filiter
only for personal use
From:fakeyw(10miric)
=====================
Waiting for Update->
*************************
1.Better
Divide the functions is Foolish
So i will restore them after
toooooooo much repeat!!!!
*************************

2.Stronger
BASIC FUNCTIONS----------
show all
Change dbs
Change table
Creat dbs
Creat table
Change user
(Add grant?)
ADVANCED FUNCTIONS -------
Add new param to table
	ensure type&length
Got all dbs&tables Given choices on UI
Add filter choices
Add Login page
User management

*************************
3:Easier
Auto commit box [√]
Muti insert
Front part UI
Dynamic tables display(auto) 
//集成函数后，每次返回的json中 附带返回【当前表】状态
//切换表，则是发送特定信息，只返回表状态
=======================================================
Standered response JSON:
{
	"type":(1,2,...)		//1:sure  2:error
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

@app.route('/search',methods=['POST'])
def search_from_dbs():
	res=''
	msg=request.form['message']
	print('[searching: %s]'% msg)
	try:
		print('ORDER: SELECT * FROM new WHERE name=%s' % msg)
		cursor.execute('SELECT * FROM new WHERE name=%s' % msg) # name=1 or 1=1 XXX msg is number
	except pymysql.err.InternalError as e:
		#print('e1')
		#print(dir(e))
		#res=e.args[0]+' '+e.args[1]
		#print(e.args)
		res='%s %s'%e.args
		res=dict(type=2,response=res)
		#logging.exception(e)
	except pymysql.err.ProgrammingError as e:
		#print('e2')
		#print(dir(e))
		#print(e.args)
		#print(type(e.args[0]))
		res='%s %s'%e.args
		#print(res)
		#print(e.args)
		res=dict(type=2,response=res)
		#logging.exception(e)  #give all error on cmd
	else:
		re=cursor.fetchall()
		length=len(re)
		res=dict(type=1,length=length,response=re)
	finally:
		res=json.dumps(res)
		print("!RES!:")
		print(res)
		return res,200,{'Access-Control-Allow-Origin':'*'}


@app.route('/insert',methods=['POST'])
def insert():
	msg=request.form['ist']
	print('Insert(Json):',msg)
	ist=json.loads(msg)
	print('list:',ist)
	if type(ist[0])!=int or type(ist[1])!=int or type(ist[2])!=int :
		res='Test ver. All input should be int 23333'
		res=dict(type=2,response=res)
	else:
		try:
			cursor.execute('INSERT INTO new VALUES(%d,%d,%d)' % (ist[0],ist[1],ist[2]))
		except pymysql.err.InternalError as e:
			res='%s %s'%e.args
			res=dict(type=2,response=res)
			#logging.exception(e)
		except pymysql.err.ProgrammingError as e:
			res='%s %s'%e.args
			res=dict(type=2,response=res)
			#logging.exception(e)
		else:
			res='Succeed!'
			res=dict(type=1,response=res)
		finally:
			res=json.dumps(res)
			return res,200,{'Access-Control-Allow-Origin':'*'}
	res=json.dumps(res)
	return res,200,{'Access-Control-Allow-Origin':'*'}

@app.route('/commit',methods=['POST'])
def commit():
	try:
		conn.commit()
	except:
		#logging.exception()
		pass
	else:
		res='Commited!'
		res=dict(type=1,response=res)
	finally:
		res=json.dumps(res)
		return res,200,{'Access-Control-Allow-Origin':'*'}
	
@app.route('/delete',methods=['POST'])
def delete():
	msg=request.form['del']
	print('Delete-name:%s' % msg)
	try:
		cursor.execute('DELETE FROM new WHERE name=%s' % msg)
	except pymysql.err.InternalError as e:
		res='%s %s'%e.args
		res=dict(type=2,response=res)
		#logging.exception(e)
	except pymysql.err.ProgrammingError as e:
		res='%s %s'%e.args
		res=dict(type=2,response=res)
		#logging.exception(e)
	else:
		res='Succeed!'
		res=dict(type=1,response=res)
	finally:
		res=json.dumps(res)
		return res,200,{'Access-Control-Allow-Origin':'*'}
	

@app.route('/',methods=['GET'])	
def search_main():
	return render_template('simple_ajax.html'),200,{'Access-Control-Allow-Origin':'*'}
	
if __name__=='__main__':
    app.run(debug=True,port=8819)