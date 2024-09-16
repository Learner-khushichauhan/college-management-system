import pyodbc as p
def myLogin():
    print("*******************LOGIN PAGE*********************")
    log_id=input("Enter the Login:->  ")
    password = input("Enter the Passswrod:->  ")
    con = p.connect('Driver={SQL Server};'
                        'Server=OM;'
                          'Database=my_Projects;'
                          'login=sa;'
                          'Password=niit'
                          'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute('''
                   Select * from New_Account where Login_Id=? and Password=?''',
                   (log_id,password))
    result=cursor.fetchall()
    if result:
        print("Login Successfully")
    else:
        print("Invalid id and Password")
        con.commit()
myLogin()