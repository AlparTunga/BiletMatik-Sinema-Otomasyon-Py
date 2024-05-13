from chair import Chair
import sqlite3 as sql
class Musteri(Chair):
    def __init__(self, name, surname, age, chair, sinema, seans):
        super().__init__(name, surname, age, chair, sinema, seans)
    def add_customer(self):
        
        conn=sql.connect('Musteri.db')
        cursor=conn.cursor()
        add_command="""INSERT INTO CUSTOMERS VALUES {}"""
        data=(self.name,self.surname,self.age,self.chair,self.sinema,self.seans)
        cursor.execute(add_command.format(data))
            
        conn.commit()
        conn.close()
    def delete_customer(self):
        conn=sql.connect('Musteri.db')
        cursor=conn.cursor()
        data=self.name
        delete_commnad=cursor.execute(f"""DELETE from CUSTOMERS WHERE name='{data}' """)
        conn.commit()
        conn.close()
