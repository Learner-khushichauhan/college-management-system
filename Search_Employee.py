import pyodbc as p 
def Del_Emp():
    print("************************************************")
    print("*               SEARCH EMPLOYEE                *")
    print("************************************************")
    cont=input('Enter the Contact Number:-> ')
    con = p.connect('Driver={SQL Server};'
                        'Server=OM;'
                          'Database=my_Projects;'
                          'login=sa;'
                          'Password=niit'
                          'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute('''
                   Select * from Employee_Details where Contact_Number=?
                   ''',cont)
    result = cursor.fetchall()
    if result:
        print("Data find success") 
        print(result)
    else:
        print("missing")
    con.commit()
Del_Emp()