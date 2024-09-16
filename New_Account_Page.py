import pyodbc as p
def New_Account():
    print("************ !!CREATE A NEW ACCOUNT!!*************")
    first_name=input("Enter the First Name:->          ")
    last_name=input("Enter the Last Name:->            ")
    gender=input("Enter the Gender:->                  ")
    dob=input("Enter the Date of Birth:->              ")
    cont_number=int(input("Enter Contact No:->         "))
    contact=str(cont_number)#type casting
    email_Id=input("Enter the Email Id:->              ")
    login_Id=input("Enter the Login_Id:->              ")
    password=input("Enter the Password:->              ")
    cnf_password=input("Enter the confirm-Password:->  ")
    #compare the Passowd and confirm Password:
    if password==cnf_password:
        #Connection python to ms sql
        con = p.connect('Driver={SQL Server};'
                            'Server=OM;'
                              'Database=my_Projects;'
                              'login=sa;'
                              'Password=niit'
                              'Trusted_Connection=yes;')
        cursor = con.cursor()
        cursor.execute('''insert into New_Account values(?,?,?,?,?,?,?,?)''',
                       first_name,last_name,gender,dob,contact,email_Id,login_Id,password);
        print('Account Created success.....')
        con.commit()
    else:
        print("password and Confirm password did not match")
New_Account()