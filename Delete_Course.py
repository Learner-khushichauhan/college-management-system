import pyodbc as p 
def Del_Course():
     print("************************************************")
     print("*               DELETE COURSE                *")
     print("************************************************")
     cid=input('Enter the Course ID:-> ')
     con = p.connect('Driver={SQL Server};'
                         'Server=OM;'
                           'Database=my_Projects;'
                           'login=sa;'
                           'Password=niit'
                           'Trusted_Connection=yes;')
     cursor = con.cursor()
     cursor.execute('''
                   DELETE  from Course_Details where Course_id=?
                    ''',cid)
     con.commit()
     print(cursor.rowcount, "record(s) deleted")
Del_Course()