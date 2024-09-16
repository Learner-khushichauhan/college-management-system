import pyodbc as p
def Update_Course():
     print("********* Update Course Detail's ************")
     eid=int(input('Enter the Course ID: '))
     emp_id=str(eid)
     Course_name=input("Enter the Course Name:->         ")
     Course_fee=input("Enter the Course Fee:->           ")
     Course_duration=input("Enter the Course Duraion:->  ")
     con = p.connect('Driver={SQL Server};'
                         'Server=OM;'
                           'Database=my_Projects;'
                           'login=sa;'
                           'Password=niit'
                           'Trusted_Connection=yes;')
     cursor = con.cursor()
     cursor.execute('''Update Course_Details set Course_name=?,Course_fee=?,Course_duration=?''',Course_name,Course_fee,Course_duration);
     k=cursor.rowcount
     if k>0:
         print('Data update success.')
     else:
         print("Some missing.")
Update_Course()   