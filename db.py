import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="", #nombre de la base de datos
        user=os.environ[''], #usuario de la bd
        password=os.environ[''])

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
