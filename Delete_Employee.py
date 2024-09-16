import pyodbc as p 
def Del_Emp():
    print("************************************************")
    print("*               SEARCH EMPLOYEE                *")
    print("************************************************")
    cont=input('Enter the contact:-> ')
    con = p.connect('Driver={SQL Server};'
                        'Server=OM;'
                          'Database=my_Projects;'
                          'login=sa;'
                          'Password=niit'
                          'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute('''
                  DELETE  from Employee_Details where Contact_Number=?
                   ''',cont)
    con.commit()
    print(cursor.rowcount, "record(s) deleted")
Del_Emp()