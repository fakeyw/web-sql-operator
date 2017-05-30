# Hello Guys,

It's just a small kit for SQL operating.
Only have TESTING functions.
So if u wanna use it now(however i thing no one wanna do that~),
u should adapt the code urself.
All right.XD

-----------

Simple template of py-sql-easyOp 
With no filter
only for personal use
From: fakeyw(10miric)
Email:main@fakeyw.top

------

### Front Part

standard request JSON:

```javascript
{
	"type":"xxx",//(cmt,ist,dele,ser...)
	"request":	
  		[a,b,c]	//(ist,muti-info)
			a  		//(ser,dele)
			//(cmt do not need this param)
}
```
Now I wanna make it split to several parts

1. Arrange functions to some .JS documents.
2. Find better JSON structure for ALL APIs.
3. Split UI into two parts: 
   1. Function area
   2. Response area
   3. Maybe others
4. Use 'src=' load parts of functions, it'll create corresponding text area / button / choices / boxes / response at the proper place

--------

###Back Part

Waiting for Update

1.Better
Divide the functions is Foolish
So I will restore them afterwards
too much repeat!!

2.Stronger
*Basic Functions:

- [ ] Change DBS
- [ ] Change table
- [ ] Create DBS
- [ ] Create table
- [ ] Change user
- [ ] User login

*Advanced Functions:

- [x] Concise code structure					
- [ ] Read all dbs&tables and given choices
- [ ] Filter
- [ ] User grant management
- [ ] Muti-insert

3.Easier

- [ ] Auto commit choice as box
- [ ] Front part UI
- [ ] Dynamic table display

------------
Standard response JSON:
```javascript
{
	"type":(1,2,...)		//1:tableinfo(muti-info use tuple) 2:status info(onr sentence)
	("length":(1,2,...))	 //for select
	"response": //for select
		[
			[a,b,c],
			[d,e,f],
			//...
		]
		//or simple info like:
		"ERROR:......"  	//for all error
		"Succeed!..."		//for insert/delete/commit
}
```