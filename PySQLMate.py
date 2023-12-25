#WELCOME PySQLMate: A User-Friendly Python MySQL CLI Interface for Non-Programmers

"""
NOTE : THESE CONDITIONS SHOULD BE FULLFILLED : 
     1.ALREADY A TABLE NAMED USER WITH FIELDS ID INT PRIMARY KEY,NAME VARCHAR(30) NOT NULL,DATE DATE,TIME TIME 
     2.SQL RANGE IN THESE DATA TYPES : date	0001-01-01 to 9999-12-31	time	00:00:00.0000000 to 23:59:59.9999999 
"""
#WELCOME TO "PYTHON-MYSQL INTERFACE" PROGRAM

print("WELCOME TO \"PySQLMate\" PROGRAM")

#MODULES USED IN THE PROGRAM

import mysql.connector

import datetime

import csv

ihost=input("host :")
iuser=input("user :")
ipasswd=input("password :")
idatabase=input("database :")
#eg: host="localhost",user="root",passwd="IIITD",database="cafe"

#CONNECTION ESTABLISHMENT 

connector=mysql.connector.connect(host=ihost,user=iuser,passwd=ipasswd,database=idatabase)

if connector.is_connected():

     print("CONNECTION ESTABLISHED BETWEEN PYTHON AND MYSQL DATABASE :",idatabase)

cursor=connector.cursor()



#USER ACCESS HISTORY CREATIONdef users():

def users():

        name=str(input("USER NAME : "))

        noww=str(datetime.datetime.now())

        noww=noww.split(" ")

        date=str(noww[-2])

        time=str(noww[-1])

        cursor.execute("select * from user")

        a=cursor.fetchall()

        b=len(a)+1

        cursor.execute("insert into user values ({},'{}','{}','{}')".format(b,name,date,time))

users()



#LOADING OF FUNCTIONS

print('PLEASE WAIT ,PROGRAM RESOURCES ARE LOADING')



#CONNECTION UNESTABLISHMENT

def connectionunestablishment() : 

        connector.close()

        if not connector.is_connected():

            print("CONNECTION UNESTABLISHED")

        print("QUERY EXECUTED")



#COMMIT COMMAND

def com():

    connector.commit()

    print("DATA SAVED!!!!!!!!!")

    print("QUERY EXECUTED")



# TO SEE LIST OF ALL PERMANENT TABLES

def showtables():

        cursor.execute("SHOW TABLES")

        a=cursor.fetchall()

        print("[ TABLES : ]")

        for i in a:

             print(i)

        print("QUERY EXECUTED")

        



#TO CHANGE STORAGE ENGINE OF TABLE (ISAM,INNODB,etc.)

def steg():

    print('''NOTE : MYSQL OFFER DIFFERENT STORAGE ENGINES FOR DIFFERENT PURPOSE ,SOME COMMON ENGINES : \n	MYISAM	:	DEFAULT STORAGE ENGINE,DOESN’T SUPPORT FOREIGN KEYS \n 	INNODB	:	SUPPORT FOREIGN KEYS ''')

    TABLENAME=str(input("TABLENAME :"))

    ENGINE=str(input("ENGINE :"))

    cursor.execute("alter table {} engine = {}".format(TABLENAME,ENGINE))

    print("QUERY EXECUTED")



#TO PERFORM SIMPLE CALCULATION BESIDE TABLE

def scal():

        cal=str(input("CALCULATION :"))

        cursor.execute("SELECT {}".format(cal))

        print("[ ",cal," ]")

        a=cursor.fetchall()

        for i in a:

             print(i)

        print("QUERY EXECUTED")



#TO DELETE DATA FROM TABLE

def dell():

    table_name=str(input("TABLE NAME :"))    

    CONDITION=str(input("CONDITION  (if not any condition ,just enter) :"))

    if CONDITION=="":

        cursor.execute("DELETE FROM {} ".format(table_name))

    else :

        cursor.execute("DELETE FROM {} WHERE {} ".format(table_name,CONDITION))

    print("QUERY EXECUTED")



# TO VIEW STRUCTURE OF A TABLE

def desc():

        des=str(input("TABLE NAME :"))

        cursor.execute("describe {}".format(des))

        print("[ Field | Type | Null | Key | Default | Extra ]")

        a=cursor.fetchall()

        for i in a:

             print(i)

        print("QUERY EXECUTED")



#TO PERFORM SQL TABLE JOINS

def sqljoin():

     way = int(input("FOR :- \n EQUI JOIN : TYPE 1 \n NATURAL JOIN : TYPE 2"))

     if way==1:

          tables=[]

          ps=[]

          n=int(input("NO. OF TABLES :"))

          while n<0:

               table=str(input("TABLE NAME : "))

               p=str(input("PRIMARY KEY OF ABOVE TABLE : "))

               tables.append(table)

               ps.append(p)

               n-=1

          t1=''

          t2=''

          

          for i in range(0,len(tables)-1):

               t1+=tables[i]+","

               t2+=tables[i]+"."+ps[i]+"="

          t1+=tables[-1]

          t2+=tables[-1]+"."+ps[-1]

          dis=str(input("DO YOU WANT TO TAKE DISTINCT QUERIES (Y/N) :"))

          if dis == 'Y' :

               dis="DISTINCT"

          elif dis == 'N' :

               dis=""

          else :

               print("error")

          columns=""

          n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

          if n=="*":

               columns="*"

          else :

               for i in range (1,n):

                    COLUMENAME=str(input("COLUMN NAME :"))

                    columns=columns+COLUMENAME+","

               COLUMENAME=str(input("COLUMN NAME :"))

               columns=columns+COLUMENAME

          CONDITION=str(input("CONDITION  (if not any condition ,type None) :"))

          if CONDITION==None:

               cursor.execute("SELECT {} {} FROM {} WHERE {} ".format(dis,columns,t1,t2))

               a=cursor.fetchall()

               print("[ ",columns," ]")

               for i in a:

                    print(i)

          else :

               cursor.execute("SELECT {} {} FROM {} WHERE {} and {}".format(dis,columns,t1,t2,CONDITION))

               a=cursor.fetchall()

               print("[ ",columns," ]")

               for i in a:

                    print(i)

          print("QUERY EXECUTED")     

     if way ==2:

          tables=''

          nt=int(input("NO. OF TABLES :"))

          nt-=1

          while nt<0:

               table=str(input("TABLE NAME : "))

               tables+=table+"," 

               nt-=1

          table=str(input("TABLE NAME : "))

          tables+=table          

          columns=""

          n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

          if n=="*":

               columns="*"

          else :

               for i in range (1,n):

                    COLUMENAME=str(input("COLUMN NAME (IF YOU WANT ANY SCALER EXPRESSIONS & ALIAS NAME WITH COLUMN ,THEN TYPE IN THIS LINE BUT AFTER COLUMN NAME BUT PUT SCALER EXPRESSION FIRST AND IF YOU WANT TO USE IFNULL CLAUSE AND WRITE IN THIS LIKE THIS (IFNULL(COLUMNNAME,\'TEXT\'))) :"))

                    columns=columns+COLUMENAME+","

               COLUMENAME=str(input("COLUMN NAME (IF YOU WANT ANY SCALER EXPRESSIONS & ALIAS NAME WITH COLUMN ,THEN TYPE IN THIS LINE BUT AFTER COLUMN NAME BUT PUT SCALER EXPRESSION FIRST AND IF YOU WANT TO USE IFNULL CLAUSE AND WRITE IN THIS LIKE THIS (IFNULL(COLUMNNAME,\'TEXT\'))) :"))

               columns=columns+COLUMENAME

          CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

          

          if CONDITION==None:

               cursor.execute("SELECT {} FROM {} ".format(columns,tables))

               a=cursor.fetchall()

               print("[ ",columns," ]")

               for i in a:

                    print(i)

          else :

               cursor.execute("SELECT {} FROM {} WHERE {}".format(columns,tables,CONDITION))

               a=cursor.fetchall()

               print("[ ",columns," ]")

               for i in a:

                    print(i)

          print("QUERY EXECUTED")         



#TO PERFORM AGGREGATE/GROUP FUNCIONS

def af():

     way =int(input("WHICH AGGREGATE/GROUP FUNCION YOU WANT TO USE : \n \t 1.AVG (TYPE 1) \n \t 2.COUNT (TYPE 2) \n \t 3.MAX (TYPE 3) \n \t 4.MIN (TYPE 4) \n \t 5.SUM (TYPE 5) "))

     if way ==  1:

          way="AVG"

     if way ==  2:

          way="COUNT"

     if way ==  3:

          way="MAX"

     if way ==  4:

          way="MIN"

     if way ==  5:

          way="SUM"

     table=str(input("TABLE NAME : "))

     COLUMENAME=str(input("COLUMN NAME :"))

     alias=str(input( "ANY ALIAS NAME \n (IF YOU DON\'T WANT TO WRITE ,THEN TYPE None) :"))

     if alias=="None":

               cursor.execute("SELECT {}({}) FROM {}".format(way,COLUMENAME,table))

               a=cursor.fetchall()

               print("[ ",way,"(",COLUMENAME,")"," ]")

               for i in a :

                    print(i)

     else :

          cursor.execute("SELECT {}({}) FROM {}".format(way,COLUMENAME,table))

          a=cursor.fetchall()

          print("[ ",alias," ]")

          for i in a:

               print(i)

     print("QUERY EXECUTED")



#MODIFYING DATA WITH UPDATE COMMAND

def ut():

     table=str(input("TABLE NAME : "))

     n=int(input("NO. OF COLUMNS"))

     columns=""

     for i in range (1,n):

          COLUMENAME=str(input("COLUMN NAME:"))

          a=str(input("VALUE OR EXPRESSION TO SET:"))

          columns=columns+COLUMENAME+"="+a+","

     COLUMENAME=str(input("COLUMN NAME:"))

     a=str(input("VALUE OR EXPRESSION TO SET:"))

     columns=columns+COLUMENAME+"="+a

     CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

     

     if CONDITION==None:

          cursor.execute("UPDATE {} SET {} ".format(table,columns))

     else :

          cursor.execute("UPDATE {} SET {} WHERE {}".format(table,columns,CONDITION))

     print("QUERY EXECUTED")



#TO INSERT VALUES IN A TABLE

def insert():

    table=str(input("TABLE NAME :"))

    values=""

    cursor.execute("DESC {}".format(table))

    a=cursor.fetchall()

    for i in range(0,len(a)-1):

         print(a[i][0]," :",end="")

         VALUE=str(input("VALUE :"))

         values=values+VALUE+","

    print(a[-1][0]," :",end="")

    VALUE=str(input("VALUE :"))

    values=values+VALUE

    cursor.execute('INSERT INTO {} VALUES ({})'.format(table,values))

    print("QUERY EXECUTED")



#VIEWING TABLE

def select() :

        table=str(input("TABLE NAME :"))           

        dis=str(input("DO YOU WANT TO TAKE DISTINCT QUERIES (Y/N) :"))

        if dis == 'Y' :

                dis="DISTINCT"

        elif dis == 'N' :

                dis=""         

        else :

                print("error")

        columns=""

        fields=""

        n=input("NO. OF COLUMNS(if all then type (*)) : ")

        if n=="*":

                columns="*"

                cursor.execute("describe {}".format(table))

                m=cursor.fetchall()

                for l in range(0,len(m)-1):

                        fields+=m[l][0] + " | "

                fields += m[-1][0]

        else :              

                for i in range (1,int(n)):

                        COLUMENAME=str(input("COLUMN NAME :"))

                        columns=columns+COLUMENAME+","

                        fields+=COLUMENAME+ " | "

                COLUMENAME=str(input("COLUMN NAME :"))

                columns=columns+COLUMENAME

                fields+=COLUMENAME

        CONDITION=str(input("ANY CONDITION  (if not any condition ,just enter)"))

        if CONDITION=="":

             cursor.execute("select {} {} from {} ".format(dis,columns,table))

             a=cursor.fetchall()

             print("[ ",fields," ]")

             for i in a:

                  print(i)

        else :

             cursor.execute("select {} {} from {} where {}".format(dis,columns,table,CONDITION))

             a=cursor.fetchall()

             print("[ ",fields," ]")

             for i in a:

                  print(i)

        print("QUERY EXECUTED")



#USER ACCESS HISTORY

def history():

     cursor.execute("desc user")

     fields=""

     m=cursor.fetchall()

     for l in range(0,len(m)-1):

          fields+=m[l][0] + " | "

     fields += m[-1][0]

     cursor.execute("select * from user")

     a=cursor.fetchall()

     print("[ ",fields," ]")

     for i in a:

          print(i)     



#CREATING TABLE

def ct():

    tables=str(input("TABLE NAME:"))

    columns=""

    n=int(input("NO. OF COLUMNS : "))

    for i in range (1,n):

        COLUMENAME=str(input("COLUMN NAME <DATATYPE> <CONSTRAINTS> :"))

        columns=columns+COLUMENAME+","

    COLUMENAME=str(input("COLUMN NAME <DATATYPE> <CONSTRAINTS> :"))

    columns=columns+COLUMENAME

    cursor.execute("create table {} ({})".format(tables,columns))

    print("QUERY EXECUTED")



#CREATING TABLE FROM EXISTING TABLE

def ctt():

    NEWTABLE=str(input("NEW TABLE :"))

    EXISTINGTABLE=str(input("EXISTINGTABLE :"))

    columns=""

    n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

    if n=="*":

        columns="*"

    else :              

        for i in range (1,n):

                COLUMENAME=str(input("COLUMN NAME :"))

                columns=columns+COLUMENAME+","

        COLUMENAME=str(input("COLUMN NAME  :"))

        columns=columns+COLUMENAME

    CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

    if CONDITION==None:

        cursor.commit("CREATE TABLE {} AS (SELECT {} FROM {})".format(NEWTABLE,columns,EXISTINGTABLE))

    else :

        cursor.commit("CREATE TABLE {} AS (SELECT {} FROM {} WHERE {})".format(NEWTABLE,columns,EXISTINGTABLE,CONDITION))

    print("QUERY EXECUTED")



#INSERTING DATA FROM ANOTHER TABLE

def it():

    NEWTABLE=str(input("NEW TABLE :"))

    EXISTINGTABLE=str(input("EXISTING TABLE :"))

    columns=""

    columnsO=""

    n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

    for i in range (1,n):

            COLUMENAME=str(input("EXISTING TABLE COLUMN NAME :"))

            columns=columns+COLUMENAME+","

            COLUMENAMEO=str(input("NEW TABLE COLUMN NAME :"))

            columnsO=columnsO+COLUMENAMEO+","

    COLUMENAME=str(input("EXISTING TABLE COLUMN NAME  :"))

    columns=columns+COLUMENAME

    COLUMENAMEO=str(input("NEW TABLE COLUMN NAME  :"))

    columnsO=columnsO+COLUMENAMEO

    CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

    if CONDITION==None:

        cursor.execute("INSERT INTO {} ({}) SELECT {} FROM {}".format(NEWTABLE,columnsO,columns,EXISTINGTABLE))

    else :

        cursor.execute("INSERT INTO {} ({}) SELECT {} FROM {} WHERE {}".format(NEWTABLE,columnsO,columns,EXISTINGTABLE,CONDITION))

    print("QUERY EXECUTED")



#DELETE TABLE

def dellt():

    table_name=str(input("table_name :"))

    cursor.execute("DROP TABLE {} ",(table_name))



#CREATE VIEW

def createview() :

    VIEWNAME=str(input("VIEWNAME"))

    BASETABLENAME=str(input("BASETABLENAME"))

    columns=""

    n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

    if n=="*":

        columns="*"

    else :              

        for i in range (1,n):

                COLUMENAME=str(input("COLUMN NAME :"))

                columns=columns+COLUMENAME+","

        COLUMENAME=str(input("COLUMN NAME  :"))

        columns=columns+COLUMENAME

    CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

    if CONDITION==None:

        cursor.execute("CREATE VIEW {} AS SELECT {} FROM {} ".format(VIEWNAME,columns,BASETABLENAME))

    else :

        cursor.execute("CREATE VIEW {} AS SELECT {} FROM {} WHERE {}".format(VIEWNAME,columns,BASETABLENAME,CONDITION))       

    print("QUERY EXECUTED")



#CONVERT A TABLE INTO CSV FILE

def convert():

    tables=str(input("TABLE NAME :"))

    filename=str(input("FILE NAME :"))

    filename+=".csv"

    f=open(filename,'w',newline='')

    fields=[]

    cursor.execute("desc {}".format(tables))

    a=cursor.fetchall()

    for i in a:

            fields.append(i[0])

    csv.writer(f).writerow(fields)

    cursor.execute("select * from {} ".format(tables))

    data=cursor.fetchall()

    list1=[]

    for k in data:

        a=[]

        for j in k:

            a.append(j)

        list1.append(a)

    csv.writer(f).writerows(list1)

    f.close()

    print("QUERY EXECUTED")



#SELECTION USING GROUP BY AND HAVING CLAUSE

def group():

    tables=str(input("TABLE NAME:"))

    columns=""

    n=int(input("NO. OF COLUMNS(if all then type (*)) : "))

    if n=="*":

        columns="*"

    else :              

        for i in range (1,n):

                COLUMENAME=str(input("COLUMN NAME :"))

                columns=columns+COLUMENAME+","

        COLUMENAME=str(input("COLUMN NAME  :"))

        columns=columns+COLUMENAME

    Ocolumns=""

    On=int(input("NO. OF COLUMNS(if all then type (*)) : "))            

    for i in range (1,On):

            OCOLUMENAME=str(input("COLUMN NAME :"))

            Ocolumns=Ocolumns+OCOLUMENAME+","

    OCOLUMENAME=str(input("COLUMN NAME  :"))

    Ocolumns=Ocolumns+OCOLUMENAME

    CONDITION=str(input("CONDITION  (if not any condition ,type None)"))

    if CONDITION==None:

        cursor.execute("SELECT {} FROM {} GROUP BY {} ".format(tables,columns,Ocolumns))

    else :

        cursor.execute("SELECT {} FROM {} GROUP BY {} HAVING {}".format(tables,columns,Ocolumns,CONDITION))       

    print("QUERY EXECUTED")



#ALTER TABLE

def alter():

        way=int(input("ALTER TABLE COMMANDS\n\t1.ADDING COLUMNS\n\t2.MODIFYING COLUMN DEFINATIONS\n\t3.CHANGING A COLUMN NAME\n\t4.REMOVING TABLE COMPONENTS\n\tNOTE\t:\tTO RUN ANY QUERY ,ENTER IT\'S SERIAL NUMBER AT RUN\n RUN\t:"))

        if way==1:

                tables=str(input("TABLE NAME:"))

                columns=""

                n=int(input("NO. OF COLUMNS) : "))          

                for i in range (1,n):

                        COLUMENAME=str(input(" <COLUMNNAME> <DATATYPE> <SIZE> [<CONSTRAINTNAME>] :"))

                        columns=columns+COLUMENAME+","

                COLUMENAME=str(input(" <COLUMNNAME1> <DATATYPE> <SIZE> [<CONSTRAINTNAME>]  :"))

                columns=columns+COLUMENAME

                cursor.execute("ALTER TABLE {} ADD ( {} )".format(tables,columns))

                print("QUERY EXECUTED")

        if way==2:

                tables=str(input("TABLE NAME:"))

                columns=str(input(" <COLUMNNAME> <NEWDATATYPE> (<NEWSIZE>) [FIRST|AFTER COLUMN]  :"))

                cursor.execute("ALTER TABLE {} MODIFY ( {} )".format(tables,columns))

                print("QUERY EXECUTED")

        if way==3:

                tables=str(input("TABLE NAME:"))

                columns=str(input("<OLDCOLUMNNAME> <NEWCOLUMNNAME> <NEWCOLUMNDEFINATION>  :"))

                cursor.execute("ALTER TABLE {} CHANGE {}".format(tables,columns))

                print("QUERY EXECUTED")

        if way==4:

                tables=str(input("TABLE NAME:"))

                columns=""

                n=int(input("NO. OF COLUMNS) : "))          

                for i in range (1,n):

                        COLUMENAME=str(input("COLUMNNAME (TYPE PRIMARY KEY IF IT IS , FOREIGN KEY <COLUMNNAME> IF IT IS,ELSE TYPE COLUMN <COLUMNNAME>):"))

                        columns=columns+"DROP "+COLUMENAME+","

                COLUMENAME=str(input("COLUMNNAME (TYPE PRIMARY KEY IF IT IS , FOREIGN KEY <COLUMNNAME> IF IT IS,ELSE TYPE COLUMN <COLUMNNAME>):"))

                columns=columns+"DROP "+COLUMENAME

                cursor.execute("ALTER TABLE {} {}".format(tables,columns))

                print("QUERY EXECUTED")



#PROGRAM LOADED

prog=5

while prog!=0:

     print(".")

     prog-=1

print("PROGRAM LOADED !!,READY TO RUN QUERIES")

#ABOUT US
def aboutus():
     with open("readme.txt","r") as aboutusfile :
          for a in aboutusfile:
               print(a)
     





#MENU

setup='on'

while setup=='on':

     print(" QUERIES : \n\t1.CONNECTION UNESTABLISHMENT AND CLOSE PROGRAM\n\t2.SAVE ALL WORK OF THIS SESSION\n\t3.SEE LIST OF ALL PERMANENT TABLES \n\t4.CHANGE STORAGE ENGINE OF TABLE (ISAM,INNODB,etc.)\n\t5.PERFORM SIMPLE CALCULATION BESIDE TABLE\n\t6.VIEW STRUCTURE OF A TABLE\n\t7.DELETE DATA FROM TABLE\n\t8.PERFORM SQL TABLE JOINS\n\t9.PERFORM AGGREGATE/GROUP FUNCIONS\n\t10.MODIFYING OR UPDATE DATA\n\t11.INSERT VALUES IN A TABLE\n\t12.VIEW TABLE\n\t13.CREATE TABLE\n\t14.CREATE TABLE FROM EXISTING TABLE\n\t15.INSERT DATA FROM ANOTHER TABLE\n\t16.DELETE TABLE\n\t17.CREATE VIEW\n\t18.SEE USER ACCESS HISTORY\n\t19.CONVERT A TABLE INTO CSV FILE\n\t20.SELECTION USING GROUP BY AND HAVING CLAUSE\n\t21.ALTER TABLE(CHANGE DESIGN OF TABLE)\n\t22.READ ABOUT US\n\tNOTE\t:\tTO RUN ANY QUERY ,ENTER IT\'S SERIAL NUMBER AT RUN\n ")

     run=int(input("\tRUN\t:\t"))

     if run==1:

          print("CONNECTION UNESTABLISHMENT")

          print("\n")

          connectionunestablishment()

          print("THANK YOU USER FOR USING THIS PROGRAM")

          setup="off"

          print("\n")

     if run==2:

          print('COMMIT COMMAND')

          print("\n")

          com()

          print("\n")

     if run==3:

          print("LIST OF ALL PERMANENT TABLES")

          print("\n")

          showtables()

          print("\n")

     if run==4:

          print("TO CHANGE STORAGE ENGINE OF TABLE")

          print("\n")

          steg()

          print("\n")

     if run==5:

          print("TO PERFORM SIMPLE CALCULATION BESIDE TABLE")

          print("\n")

          scal()

          print("\n")

     if run==6:

          print("STRUCTURE OF A TABLE")

          print("\n")

          desc()

          print("\n")

     if run==7:

          print("DATA DELETION")

          print("\n")

          dell()

          print("\n")

     if run==8:

          print("SQL TABLE JOINS")

          print("\n")

          sqljoin()

          print("\n")

     if run==9:

          print("AGGREGATE/GROUP FUNCIONS")

          print("\n")

          af()

          print("\n")

     if run==10:

          print("UPDATING DATA")

          print("\n")

          ut()

          print("\n")

     if run==11:

          print("INSERTING VALUES IN A TABLE")

          print("\n")

          insert()

          print("\n")

     if run==12:

          print("VIEWING TABLE")

          print("\n")

          select()

          print("\n")

     if run==13:

          print("CREATING TABLE")

          print("\n")

          ct()

          print("\n")

     if run==14:

          print("CREATING TABLE FROM EXISTING TABLE")

          print("\n")

          ctt()

          print("\n")

     if run==15:

          print("INSERTING DATA FROM ANOTHER TABLE")

          print("\n")

          it()

          print("\n")

     if run==16:

          print("TABLE DELETION")

          print("\n")

          dellt()

          print("\n")

     if run==17:

          print("VIEW CREATION")

          print("\n")

          createview()

          print("\n")

     if run==18:

          print("USER ACCESS HISTORY")

          print("\n")

          history()

          print("\n")

     if run==19:

          print("CONVERTING TABLE INTO CSV FILE")

          print("\n")

          convert()

          print("\n")

     if run==20:

          print(" SELECTION USING GROUP BY AND HAVING CLAUSE")

          print("\n")

          group()

          print("\n") 

     if run==21:

          print("ALTERING TABLE")

          print("\n")

          alter()

          print("\n")
          
     if run==22:

          print("ABOUT US")

          print("\n")

          aboutus()

          print("\n")