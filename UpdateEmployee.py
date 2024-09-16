import pyodbc as p
def Update_Emp():
    print("********* Update Employee Detail's ************")
    eid=int(input('Enter the Employee ID: '))
    emp_id=str(eid)
    first_name=input("Enter the First Name:->          ")
    last_name=input("Enter the Last Name:->            ")
    gender=input("Enter the Gender:->                  ")
    dob=input("Enter the Date of Birth:->              ")
    dep_name=input("Enter the Dep:->                   ")
    salary=float(input("Enter the Salary:->            "))
    cont_number=int(input("Enter Contact No:->         "))
    aadhar_number=int(input("Enter Aadhar No:->       "))
    email_Id=input("Enter the Email Id:->              ")
    address=input("Enter the Address:->       ")
    sal=str(salary)
    contact=str(cont_number)
    aadhar=str(aadhar_number)
    con = p.connect('Driver={SQL Server};'
                        'Server=OM;'
                          'Database=my_Projects;'
                          'login=sa;'
                          'Password=niit'
                          'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute('''Update Employee_Details set First_Name=?,Last_Name=?,Gender=?,Date_of_Birth=?,Dep_Name=?,Salary=?,Contact_Number=?,Aadhar_Number=?,EmailID=?,Address=? where Emp_Id=?''',
                   first_name,last_name,gender,dob,dep_name,sal,contact,aadhar,email_Id,address,emp_id);
    k=cursor.rowcount
    if k>0:
        print('Data update success.')
    else:
        print("Some missing.")
Update_Emp()   