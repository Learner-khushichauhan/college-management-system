import pyodbc as p 
def Del_staff():
    print("************************************************")
    print("*               DELETE STAFF                *")
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
                  DELETE  from Other_Staff where Contact_number=?
                   ''',cont)
    con.commit()
    print(cursor.rowcount, "record(s) deleted")
Del_staff()