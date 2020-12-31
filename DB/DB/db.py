import os
import json
LOCATION=os.path.join(os.path.expanduser("~"),"Desktop")
os.chdir(LOCATION)
class DB:



    def __init__(self,path=None,filename="database"):
        self.filename=filename+".json"
        self.path=path
        try:
            os.chdir(self.path)
        except:
            self.path=os.getcwd()
        self.dbname=""
        self.key=""
        self.original=""
        self.order=list()
        self.isAlive=False
        super().__init__()





    def checkDB(self):
        try:
            with open(self.filename,"r") as f:
                database=json.load(f)
                database=""
                f.close()
            return True
        except:
            return False




    def showDB(self):
        try:
            with open(self.filename,"r") as f:
                databases=json.load(f)
                databases=list(databases.keys())
                f.close()
                return databases
        except:
            return "MESSAGE: DATABASE IS EMPTY!"







    def connect(self,dbname):
        if self.checkDB()==True:
            if self.isAlive==False:
                with open(self.filename,"r") as f:
                    database=json.load(f)
                    f.close()
                    if dbname in database:
                        #try:
                        self.dataset=database[dbname]
                        self.original=database[dbname]
                        self.dbname=dbname
                        self.key=dbname
                        self.order.append(dbname)
                        self.isAlive=True
                        #except:
                            #return 'ERROR: "'+dbname+'" DATABASE IS EMPTY! '
                    else:
                        return 'ERROR: "'+dbname+'" DATABASE NOT FOUND :('
            else:
                return "WARNING: CLOSE THE ACTIVE DATABASE("+self.dbname+") FIRST! example: db.close()"
        else:
            return "ERROR: DATABASE IS EMPTY!"






    def create(self,key,value):
        if key!="" and value!="" and value!=[] and value!={}:
            if type(key)!=str:
                return 'ERROR: "key" MUST BE A TYPE OF STRING!'
            if type(value)==tuple:
                return 'ERROR: "value" MUST NOT BE A TUPPLE!'
            else:
                if self.checkDB()==True:
                    if self.isAlive==True:
                        if type(self.dataset)!=dict:
                            return "ERROR: INVALID OPERATION ON ATOMIC KEY-VALUE PAIR!"
                        else:
                            if key in self.dataset:
                                return 'WARNING: "'+key+'" KEY ALREADY EXISTS!'
                            else:
                                string="database"
                                for sequence in self.order:
                                    string=string+'["'+str(sequence)+'"]'
                                if type(value)==str:
                                    string=string+'.update({"'+str(key)+'":"'+str(value)+'"})'
                                else:
                                    string=string+'.update({"'+str(key)+'":'+str(value)+'})'


                                with open(self.filename,'r') as f:
                                    database=json.load(f)
                                    f.close()
                                    eval(string)
                                with open(self.filename,'w') as f:
                                    try:
                                        f.write(str(json.dumps(database)))
                                        
                                    except:
                                        pass
                                    finally:
                                        f.close()
                                
                                self.original=database[self.dbname]
                                try:
                                    self.dataset=self.original[self.order[-1]]
                                except:
                                    pass
                    else:
                        with open(self.filename,'r') as f:
                            database=json.load(f)
                            f.close()
                            if key in database:
                                return 'WARNING: "'+key+'" DATABASE ALREADY EXISTS!'
                            else:
                                database.update({key:value})
                                with open(self.filename,'w') as f:
                                    f.write(str(json.dumps(database)))
                                    f.close()
                else:
                    database={key:value}
                    with open(self.filename,'w') as f:
                         f.write(str(json.dumps(database)))
                         f.close()
                    
                    
        else:
            return 'ERROR: "key" AND "value" MUST NOT BE EMPTY!'
        






    def read(self,instance):
        try:
            if self.dbname==instance:
                return self.original
            elif self.key==instance:
                try:
                    return self.dataset[instance]
                except:
                    return self.dataset
            elif instance in self.dataset:
                try:
                    return self.dataset[instance]
                except:
                    return self.dataset[instance]
            else:
                return 'ERROR: "'+instance+'" IS NOT A VALID KEY OR A SCOPE KEY'
        except:
            return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"






    def select_parent(self):
        if self.isAlive==True:
            try:
                if self.order==[]:
                    self.select_root()
                else:
                    self.order.pop()
                    self.key=""
                    self.dataset=self.original[self.order[len(self.order)-1]]
            except:
                self.select_root()
        else:
            return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"






        
    def select_root(self):
        if self.isAlive==True:
            try:
                self.dataset=self.original
                self.order=[]
                self.order.append(self.dbname)   
            except:
                return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"
        else:
            return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"




    def select(self,instance):
        if self.isAlive==True:
            try:
                if self.key==instance:
                    return "WARNING: ALREADY SELECTED KEY!"
                elif instance in self.dataset:
                    if type(self.dataset[instance])==dict:
                        self.key=instance
                        self.order.append(instance)
                        self.dataset=self.dataset[instance]
                    else:
                        return 'ERROR: "'+instance+'" IS ATOMIC KEY NOT A COLLECTION OBJECT!'
                else:
                    return 'ERROR:"'+instance+'" IS NOT A VALID KEY OR db OBJECT'
            except:
                return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"
        else:
            return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"





        

    def delete(self,instance):
        if self.isAlive==True:
            if type(instance)!=str:
                return 'ERROR: "key" MUST BE STRING TYPE'
            else:
                if self.isAlive==True:
                    if instance in self.dataset:
                        string="database"
                        for sequence in self.order:
                            string=string+'["'+str(sequence)+'"]'
                        string=string+'.pop("'+str(instance)+'")'
                        with open('database.json','r') as f:
                            database=json.load(f)
                            f.close()
                            eval(string)
                        with open(self.filename,'w') as f:
                            try:
                                f.write(str(json.dumps(database)))
                            except:
                                pass
                            finally:
                                f.close()
                        self.original=database[self.dbname]
                        try:
                            self.dataset=self.original[self.order[-1]]
                        except:
                            pass
                    else:
                        return 'ERROR: INVALID "key" OR KEY IS NOT IN THIS SCOPE!'
                else:
                    try:
                        with open(self.filename,'r') as f:
                            databases=json.load(f)
                            f.close()
                            if instance in databases:
                                databases.pop(instance)
                                with open(self.filename,'w') as f:
                                    try:
                                        f.write(str(json.dumps(databases)))
                                    except:
                                        pass
                                    finally:
                                        f.close()
                            else:
                                return 'ERROR: NO DATABASE FOUND!'
                    except:
                        return "ERROR: SOMETHING WENT WRONG!"
        else:
            return "ERROR: FIRST CONNECT TO A DATABASE, EXAMPLE: db.connect('dbname')"






        
    def close(self):
        if self.dbname:
            self.dataset=""
            self.dbname=""
            self.original=""
            self.key=""
            self.isAlive=False
            self.order=[]
        else:
            return "WARNING: NO ACTIVE DATABASE FOUND!"

if __name__=="__main__":
    from db import DB
