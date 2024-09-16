import pyodbc as p
def Update_staff():
    print("********* Update Other_staff Detail's ************")
    eid=int(input('Enter the Staff_ID: '))
    emp_id=str(eid)
    name=input("Enter the  Name:->          ")
    gender=input("Enter the Gender:->                  ")
    dep_name=input("Enter the Dep:->                   ")
    salary=float(input("Enter the Salary:->            "))
    cont_number=int(input("Enter Contact No:->         "))
    aadhar_number=int(input("Enter Aadhar No:->       "))
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
    cursor.execute('''Update Other_Staff set Name=?,Gender=?,Dep_name=?,
                   Salary=?,Contact_number=?,Aadhar_number=?
                   where Emp_id=?''',
                   name,gender,dep_name,sal,contact,aadhar,emp_id);
    k=cursor.rowcount
    if k>0:
        print('Data update success.')
    else:
        print("Some missing.")
Update_staff()   