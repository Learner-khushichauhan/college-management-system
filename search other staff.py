import pyodbc as p 
def ser_staff():
    print("************************************************")
    print("*               SEARCH OTHER_STAFF                *")
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
                   Select * from Other_Staff where Contact_number=?
                   ''',cont)
    result = cursor.fetchall()
    if result:
        print("Data find success") 
        print(result)
    else:
        print("missing")
    con.commit()
ser_staff()