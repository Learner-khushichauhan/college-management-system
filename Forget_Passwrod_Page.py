import pyodbc as p
def Forget_Password():
    print("*************Update Password*************")
    cont = int(input('Enter the Contact Number: '))
    contact = str(cont)
    new_password = input('Enter the Password: ')
    conf_password=input('Enter the Confirm Password: ')
    if new_password==conf_password:
        con = p.connect('Driver={SQL Server};'
                            'Server=OM;'
                              'Database=my_Projects;'
                              'login=sa;'
                              'Password=niit'
                              'Trusted_Connection=yes;')
        cursor = con.cursor()
        cursor.execute('''Update New_Account set Password=? where Contact_Number=?''',
                       new_password,contact);
        print('Password Update Success.....')
        con.commit()
    else:
        print('Password and Confirm Password did not match.')
Forget_Password()