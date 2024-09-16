import pyodbc as p 
def Search_Course():
      print("************************************************")
      print("*               SEARCH COURSE                  *")
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
                     Select * from Course_Details where Course_id=?
                     ''',cid)
      result = cursor.fetchall()
      if result:
          print("Data find success") 
          print(result)
      else:
          print("missing")
      con.commit()
Search_Course()