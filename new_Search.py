import pyodbc as p 
import pandas as pd
def Del_Emp():
    #cont=input('Enter the cont')
    con = p.connect('Driver={SQL Server};'
                        'Server=OM;'
                          'Database=my_Projects;'
                          'login=sa;'
                          'Password=niit'
                          'Trusted_Connection=yes;')
    query = "SELECT * from Employee_Details;"
    df = pd.read_sql(query, con)
    print(df)
Del_Emp()