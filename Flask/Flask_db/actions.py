import os
import psycopg2
from flask import Flask, render_template,request, redirect, url_for
def get_db_connection():
    conn = psycopg2.connect(host = 'localhost',
                            database = 'Flask_db',
                            user = 'postgres',
                            password = 'Finserv@2023')

    return conn

conn = get_db_connection()
curr = conn.cursor()
curr.execute('DELETE FROM books WHERE id = 2')
curr.execute(' SELECT * FROM books')
print(curr.fetchall)
conn.commit()
curr.close()
conn.close()
