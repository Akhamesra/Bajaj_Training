import psycopg2

class Pet:
    def __init__(self,pname,pbreed,oname):
        self.pname = pname
        self.pbreed =pbreed
        self.oname = oname

class DBconnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(self):
        self.conn = psycopg2.connect(host = 'localhost',
                            database = 'Flask_db',
                            user = 'postgres',
                            password = 'Finserv@2023')
        self.cur = self.conn.cursor()

    @classmethod
    def create_table(self,tablename,f1,f2,f3):
        self.cur.execute('CREATE TABLE '+ str(tablename)+'(' + str(f1)+ ' varchar primary key,' + str(f2) + ' varcahr,' + str(f3) + ' varchar);')
        self.conn.commit()

    @classmethod
    def insert_self(self,tablename,f1,f2,f3):
        self.cur.execute('INSERT INTO '+ str(tablename)+ 'VALUES(%s, %s, %s);',(str(f1),str(f2),str(f3)))
        self.conn.commit()
    
    @classmethod
    def select_result(self,tablename):
        self.conn.execute('SELECT * FROM '+str(tablename)+';')
        students = self.cur.fetchall()
        for student in students:
            print(student)

    @classmethod
    def close(self):
        self.cur.close()
        self.conn.close()
