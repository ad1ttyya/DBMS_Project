import mysql.connector

f = open("Credentials.txt")
mydb = mysql.connector.connect(host=f.readline(),user=f.readline(),password=f.readline())
print(mydb)
f.close()
