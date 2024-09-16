import pyodbc as p
def Add_Course():
     print("********* Welcome to our Campus************")
     Course_name=input("Enter the Course Name:->          ")
     Course_Fee=int(input("Enter the Course Fee:->       "))
     Course_duration=input("Enter the Course Duration:->  ")     
     con = p.connect('Driver={SQL Server};'
                         'Server= OM'
                           'Database=my_Projects;'
                           'login=sa;'
                           'Password=niit'
                           'Trusted_Connection=yes;')
     cursor = con.cursor()
     cursor.execute('''insert into Course_Details values(?,?,?)''',Course_name,Course_Fee,Course_duration);
     print('Record Store success.....')
     con.commit()
Add_Course()