# Database
<h3>  Problem Statement </h3>
<img alt="problem_image" src="https://github.com/21170293/data/blob/master/img/assis-1.jpg" >
<h3> I made a solution of above problem in "Python"</h3>
<p>
>>> from DB.db import DB<br><br>
>>> # Now Creating an object<br><br>
>>> db=DB()<br><br>
>>> #Initially there isn't any database<br>
>>> #And the default location of the database is in desktop<br>
>>> #this is only for demonstration purpose<br>
>>> #developer can change the path and database name<br><br>
>>> db.showDB() #This function display database if there is any<br><br>
'MESSAGE: DATABASE IS EMPTY!'<br>
<h2># CREATE OPERATION</h2>
>>> #This will create a database in default location<br><br>
>>> db.create(key="newDB",value={"name":"yash shukla"})<br><br>
>>> #db is created<br><br>
>>> #no error message<br><br>
>>> db.showDB()<br><br>
['newDB']<br><br>
>>> #now we can see the newly created database<br>
>>> db.connect("newDB") #This will connect to database<br>
>>> db.connect("newDBs")<br><br>
'WARNING: CLOSE THE ACTIVE DATABASE(newDB) FIRST! example: db.close()'<br>
>>> #If any db is connect or live then above msg will appear for different cnonection request<br><br>
>>> db.close() #this function unlink the database connection<br><br>
>>> db.connect("newDBs") #This will raise an error<br><br>
'ERROR: "newDBs" DATABASE NOT FOUND :('<br><br>
>>> #there is no database named "newDBs"<br><br>
>>> #there is only one available in this time "newDB"<br><br>
>>> db.connect("newDB")<br><br>
<h2># READ OPERATION</h2>
>>> db.read("newDB") #It returns all the content of selected key<br><br>
{'name': 'yash shukla'}<br><br>
  
>>> db.create(key="address",value={"house_no":"11b/12"})<br><br>
>>> db.read("newDB")<br><br>
{'name': 'yash shukla', 'address': {'house_no': '11b/12'}}<br><br>
>>> #If we want to add key-value in nested key ex:"address"<br><br>
>>> #First select 'address'<br><br>
>>> db.select("address")<br><br>
>>> db.read("address")<br><br>
{'house_no': '11b/12'}<br><br>
>>> #the current cursor is in "address"<br><br>
>>> #now we can add new key at "address"<br><br>
>>> db.create(key="city",value="Allahabad")<br><br>
>>> db.create(key="state",value="uttar pradesh")<br><br>
>>> #two keys added to address now we can see it<br><br>
>>> db.read("address")<br><br>
{'house_no': '11b/12', 'city': 'Allahabad', 'state': 'uttar pradesh'}<br><br>
>>> #now for selecting parent key object we use<br><br>
>>> db.select_parent()<br><br>
>>> db.read("newDB")<br><br>
{<br><br>
  "name": "yash shukla",<br>
  "address": {<br>
    "house_no": "11b/12",<br>
    "city": "Allahabad",<br>
    "state": "uttar pradesh"<br>
  }<br>
}<br><br>
<h2># DELETE OPERATION</h2>
>>> #now performing deletion<br><br>
>>> #lets delete "state" from "address"<br><br>
>>> db.select("address")<br><br>
>>> db.delete("state")<br><br>
{<br>
  "name": "yash shukla",<br>
  "address": {<br>
    "house_no": "11b/12",<br>
    "city": "Allahabad"<br>
  }<br>
}<br><br>
>>> #See "state" is deleted<br>
</p>
