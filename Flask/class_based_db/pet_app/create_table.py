import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="Flask_db",
        user= 'postgres',
        password='Finserv@2023')

# Open a cursor to perform database operations
cur = conn.cursor()
# cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
#                                  'title varchar (150) NOT NULL,'
#                                  'author varchar (50) NOT NULL,'
#                                  'pages_num integer NOT NULL,'
#                                  'review text,'
#                                  'date_added date DEFAULT CURRENT_TIMESTAMP);'
#                                  )
cur.execute('CREATE TABLE pet_shop (id serial PRIMARY KEY,'
                                 'pet_name varchar (50) NOT NULL,'
                                 'pet_breed varchar (50) NOT NULL,'
                                 'owner varchar (50) NOT NULL);'
                                 )


conn.commit()

cur.close()
conn.close()