import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root', password='Emilio12345.',
                              host='127.0.0.1',
                              database='neoguias')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Nombre de Usuario o contrasena incorrecta")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Base de datos no existe")
  else:
    print(err)
else:
    print("Conexion correcta")
    cnx.close()