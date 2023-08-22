import mysql.connector
import django

cnx = mysql.connector.connect(user='root', password='Emilio12345.',
                              host='127.0.0.1',
                              database='neoguias')
if cnx=='':
  print("Conexion fallida")
else:
  print("Conexion OK")
cnx.close()