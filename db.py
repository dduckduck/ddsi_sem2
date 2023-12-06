import os
import oracledb
import datetime
#https://docs.oracle.com/javadb/10.8.3.0/devguide/cdevconceptssavepoints.html

#conf
usr = input("USUARIO:")
pwd = usr
cs = "oracle0.ugr.es:1521/practbd.oracle0.ugr.es"   
#Conexión
try:
    conn = oracledb.connect(user=usr,password=pwd,dsn=cs)
except Exception as e:
    print(f"Error al establecer coneixón: {e}\nFin del programa")
    exit(-1)

cur = conn.cursor()

# Crear tabla de libros 
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insertar datos en la tabla 
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Cronicas de la Torre',
             'Laura Gallego',
             271,
             'Libro de fantasia de adolescentes')
            )

conn.commit()

cur.close()
conn.close()
