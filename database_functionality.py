import mysql.connector

#This file deal with the interaction with the mySQL database using MySQL python connector module

def add_phone(brand,model,price,camq,proq,batq,romq,disq,ramq,cat,cam,ram,pro,bat,dis,rom,os,col,rat,pur1,pur2):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database = "projectdata"
    )

    mycursor = mydb.cursor()
    command = "INSERT INTO mobile (brand,model,price,camq,proq,batq,romq,disq,ramq,cat,cam,ram,pro,bat,dis,rom,os,col,rat,pur1,pur2) VALUES " \
           "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    input = (brand,model,price,camq,proq,batq,romq,disq,ramq,cat,cam,ram,pro,bat,dis,rom,os,col,rat,pur1,pur2)
    mycursor.execute(command,input)
    mydb.commit()
    return 'p'

def find_phone(cq,pq,bq,sq,dq,rq):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    command = "SELECT brand,model FROM mobile WHERE camq = %s AND proq = %s AND batq = %s AND romq = %s AND disq = %s AND ramq = %s"
    input = (cq,pq,bq,sq,dq,rq)
    mycursor.execute(command,input)
    result = mycursor.fetchall()
    if(len(result) == 0 ):
        return 'e'
    else:
        return result

def details(brand,model):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "SELECT * FROM mobile WHERE brand = %s AND model = %s"
    input = (brand,model)
    mycursor.execute(cmd, input)
    result = mycursor.fetchall()
    if (len(result) == 0):
        return 'e'
    else:
        return result

def internor(z='1'):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "select cat,brand,model from mobile"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    #print(result)
    j = 0
    phone = list()
    for i in result:
        a = result[j][0][0]
        #print(a)
        if(z==a):
            temp = (result[j][1],result[j][2])
            phone.append(temp)
        j+=1
    print(phone)
    return phone

def intercam(z='1'):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "select cat,brand,model from mobile"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    #print(result)
    j = 0
    phone = list()
    for i in result:
        a = result[j][0][1]
        #print(a)
        if(z==a):
            temp = (result[j][1],result[j][2])
            phone.append(temp)
        j+=1
    print(phone)
    return phone

def intertravel(z='1'):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "select cat,brand,model from mobile"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    #print(result)
    j = 0
    phone = list()
    for i in result:
        a = result[j][0][2]
        #print(a)
        if(z==a):
            temp = (result[j][1],result[j][2])
            phone.append(temp)
        j+=1
    print(phone)
    return phone

def intergame(z='1'):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "select cat,brand,model from mobile"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    
    j = 0
    phone = list()
    for i in result:
        a = result[j][0][3]
        #print(a)
        if(z==a):
            temp = (result[j][1],result[j][2])
            phone.append(temp)
        j+=1
    print(phone)
    return phone

def interprop(z='1'):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    cmd = "select cat,brand,model from mobile"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    
    j = 0
    phone = list()
    for i in result:
        a = result[j][0][4]
        #print(a)
        if(z==a):
            temp = (result[j][1],result[j][2])
            phone.append(temp)
        j+=1
    print(phone)
    return phone

def value(min,max):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projectdata"
    )

    mycursor = mydb.cursor()
    command = "SELECT brand,model FROM mobile WHERE price BETWEEN %s AND %s"
    input = (min,max)
    mycursor.execute(command, input)
    result = mycursor.fetchall()
    if (len(result) == 0):
        return 'e'
    else:
        return result


#internor()
