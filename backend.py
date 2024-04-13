import mysql.connector

f = open("Credentials.txt")
mydb = mysql.connector.connect(host=f.readline(),user=f.readline(),password=f.readline())
print(mydb)
f.close()

#to check that the import backend works
# def hello():
# print("dawdwadawdawdwad")

mycursor = mydb.cursor()
mycursor.execute("use USER_CREDENTIALS")
mycursor.execute("SELECT * FROM USER_LOGIN_DATA")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
print("\n\n")  

mycursor.execute("use COMP_DATABASE")
mycursor.execute("SELECT * FROM INVENTORY_ALL_ITEMS")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
print("\n\n")   
  
mycursor.execute( "SELECT * FROM INVENTORY_ALL_ITEMS WHERE STATUS='IN' " )
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
print("\n\n")    
  
mycursor.execute( "SELECT * FROM INVENTORY_ALL_ITEMS WHERE STATUS='OUT' " )
myresult = mycursor.fetchall()
for x in myresult:
  print(x)