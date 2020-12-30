# Database
<h3>  Problem Statement </h3>
<img alt="problem_image" src="https://github.com/21170293/data/blob/master/img/assis-1.jpg" >
<h3> I made a solution of above problem in "Python"</h3>
<p>
>>> from DB.db import DB<br>
>>> # Now Creating an object<br>
>>> db=DB()<br>
>>> #Initially there isn't any database<br>
>>> #And the default location of the database is in desktop<br>
>>> #this is only for demonstration purpose<br>
>>> #developer can change the path and database name<br>
>>> db.showDB() #This function display database if there is any<br>
'MESSAGE: DATABASE IS EMPTY!'<br>
>>> #This will create a database in default location<br>
>>> db.create(key="newDB",value={"name":"yash shukla"})<br>
>>> #db is created<br>
>>> #no error message<br>
>>> db.showDB()<br>
['newDB']<br>
>>> #now we can see the newly created database<br>
>>> db.connect("newDB") #This will connect to database<br>
>>> db.connect("newDBs")<br>
'WARNING: CLOSE THE ACTIVE DATABASE(newDB) FIRST! example: db.close()'<br>
>>> #If any db is connect or live then above msg will appear for different cnonection request<br>
>>> db.close() #this function unlink the database connection<br>
>>> db.connect("newDBs") #This will raise an error<br>
'ERROR: "newDBs" DATABASE NOT FOUND :('<br>
>>> #there is no database named "newDBs"<br>
>>> #there is only one available in this time "newDB"<br>
>>> db.connect("newDB")<br>
>>> db.read("newDB") #It returns alll the content of selected key<br>
{'name': 'yash shukla'}<br>
>>> db.create(key="address",value={"house_no":"11b/12"})<br>
>>> db.read("newDB")<br>
{'name': 'yash shukla', 'address': {'house_no': '11b/12'}}<br>
>>> #If we want to add key-value in nested key ex:"address"<br>
>>> #First select 'address'<br>
>>> db.select("address")<br>
>>> db.read("address")<br>
{'house_no': '11b/12'}<br>
>>> #the current cursor is in "address"<br>
>>> #now we can add new key at "address"<br>
>>> db.create(key="city",value="Allahabad")<br>
>>> db.create(key="state",value="uttar pradesh")<br>
>>> #two keys added to address now we can see it<br>
>>> db.read("address")<br>
{'house_no': '11b/12', 'city': 'Allahabad', 'state': 'uttar pradesh'}<br>
>>> #now for selecting parent key object we use<br>
>>> db.select_parent()<br>
>>> db.read("newDB")<br>
{<br>
  "name": "yash shukla",<br>
  "address": {<br>
    "house_no": "11b/12",<br>
    "city": "Allahabad",<br>
    "state": "uttar pradesh"<br>
  }<br>
}<br>
</p>
