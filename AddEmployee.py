import pyodbc as p
def Add_Employee():
    print("********* Welcome to our Campus************")
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
    cursor.execute('''insert into Employee_Details values(?,?,?,?,?,?,?,?,?,?)''',
                   first_name,last_name,gender,dob,dep_name,sal,contact,aadhar,email_Id,address);
    print('Record Store success.....')
    con.commit()
Add_Employee()