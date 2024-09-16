import pyodbc as p 
def Show_all_Stu():
     print("************************************************")
     print("*              SHOW ALL STUDENTS                *")
     print("************************************************")
     con = p.connect('Driver={SQL Server};'
                         'Server=OM;'
                           'Database=my_Projects;'
                           'login=sa;'
                           'Password=niit'
                           'Trusted_Connection=yes;')
     cursor = con.cursor()
     cursor.execute('SELECT * FROM Student_Details')
     for i in cursor:
         print(i)
     con.commit()
     print(cursor.rowcount, "record(s) found")
Show_all_Stu()