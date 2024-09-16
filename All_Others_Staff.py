import pyodbc as p 
def Show_all_OT():
     print("************************************************")
     print("*              SHOW ALL OTHER'S STAFF              *")
     print("************************************************")
     con = p.connect('Driver={SQL Server};'
                         'Server=OM;'
                           'Database=my_Projects;'
                           'login=sa;'
                           'Password=niit'
                           'Trusted_Connection=yes;')
     cursor = con.cursor()
     cursor.execute('SELECT * FROM Other_Staff')
     for i in cursor:
         print(i)
     con.commit()
     print(cursor.rowcount, "record(s) found")
Show_all_OT()