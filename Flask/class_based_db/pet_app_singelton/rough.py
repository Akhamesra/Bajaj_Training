import psycopg2
conn = None
cur = None
conn = psycopg2.connect(host = 'localhost',
                    database = 'Flask_db',
                    user = 'postgres',
                    password = 'Finserv@2023')
cur = conn.cursor()

