import psycopg2

class Student:
    def __init__(self,sid,sname,sadd):
        self.sid = sid
        self.sname = sname
        self.sadd = sadd

class DBconnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(cls):
        cls.conn = psycopg2.connect("dbname = postgres user=postgres password = postgres")
        cls.cur = cls.conn.cursor()

    @classmethod
    def create_table(cls,tablename,f1,f2,f3):
        cls.cur.execute('CREATE TABLE '+ str(tablename)+'(' + str(f1)+ ' varchar primary key,' + str(f2) + ' varcahr,' + str(f3) + ' varchar);')
        cls.conn.commit()

    @classmethod
    def insert_cls(cls,tablename,f1,f2,f3):
        cls.cur.execute('INSERT INTO '+ str(tablename)+ 'VALUES(%s, %s, %s);',(str(f1),str(f2),str(f3)))
        cls.conn.commit()
    
    @classmethod
    def select_result(cls,tablename):
        cls.conn.execute('SELECT * FROM '+str(tablename)+';')
        students = cls.cur.fetchall()
        for student in students:
            print(student)

    @classmethod
    def close(cls):
        cls.cur.close()
        cls.conn.close()
