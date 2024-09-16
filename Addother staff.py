import pyodbc as p
def Add_staff():
    print("********* Welcome to our Campus************")
    name=input("Enter the  Name:->                    ")
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
    cursor.execute('''insert into Other_Staff values(?,?,?,?,?,?)''',
                   name,gender,dep_name,sal,contact,aadhar);
    print('Record Store success.....')
    con.commit()
Add_staff()
 
