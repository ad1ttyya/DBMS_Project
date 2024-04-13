import mysql.connector
f = open("Credentials.txt")
mydb = mysql.connector.connect(host=f.readline(),user=f.readline(),password=f.readline())
print(mydb)
f.close()

mycursor = mydb.cursor()

def userdata():
  mycursor.execute("use USER_CREDENTIALS")
  mycursor.execute("SELECT * FROM USER_LOGIN_DATA")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def table1():#itemlist
  mycursor.execute("use COMP_DATABASE")
  mycursor.execute("SELECT * FROM INVENTORY_ALL_ITEMS")
  myresult = mycursor.fetchall()
  return myresult
  
def table2():#in_stock
  mycursor.execute("use COMP_DATABASE")
  mycursor.execute( "SELECT * FROM INVENTORY_ALL_ITEMS WHERE STATUS='IN' " )
  myresult = mycursor.fetchall()
  return myresult
  
def table3():#out_stock
  mycursor.execute("use COMP_DATABASE")
  mycursor.execute( "SELECT * FROM INVENTORY_ALL_ITEMS WHERE STATUS='OUT' " )
  myresult = mycursor.fetchall()
  return myresult

def table4(price,name,quantity,status):#add_item
  mycursor.execute("use COMP_DATABASE")
  sql = "INSERT INTO INVENTORY_ALL_ITEMS (ITEM_PRICE,ITEM_NAME,QUANTITY,STATUS) VALUES (%s, %s, %s, %s)"
  values = (price,name,quantity,status)
  mycursor.execute(sql, values)
  mydb.commit()

# table4(120 , "A4SHEET" , 470 , "IN")

def table5(name):#delete_item
  mycursor.execute("use COMP_DATABASE")
  sql = "DELETE FROM INVENTORY_ALL_ITEMS WHERE ITEM_NAME = %s"
  values = (name, )
  mycursor.execute(sql, values)
  mydb.commit()
 
# table5("A4SHEET")

def table6(price,name,quantity,status,namedelete):#edit_item
  mycursor.execute("use COMP_DATABASE")
  sql = "UPDATE INVENTORY_ALL_ITEMS SET ITEM_PRICE= %s ,ITEM_NAME= %s ,QUANTITY= %s ,STATUS= %s WHERE ITEM_NAME= %s "
  values = (price,name,quantity,status,namedelete)
  mycursor.execute(sql, values)
  mydb.commit()
  
#table6(400,"TAPE",69,"IN","TAPE")


# CREATE TABLE OUT_STOCK
# AS SELECT
#   *
# FROM INVENTORY_ALL_ITEMS
# WHERE STATUS = 'out';