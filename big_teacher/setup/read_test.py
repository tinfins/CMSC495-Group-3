import mysql.connector
import multiple_statements


mydb = mysql.connector.connect(
  host="cmsc495.cnqrtayefs7j.us-east-2.rds.amazonaws.com",
  user="admin_cmsc495",
  password="CMSC495CMSC$(%",
  database="cmsc495"
)

statements = []
with open('database_setup.sql') as stmnt:
    for line in stmnt:
        if not line.strip(): continue
        statements.append(line.strip('\n').replace("`",""))
        
multiple_statements.multiple_statements(mydb, statements, False)
#print(statements)
#for line in statements:
    #print(line)
