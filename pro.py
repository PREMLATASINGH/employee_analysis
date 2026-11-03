import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
data={
    'emp_id':[1,2,3,4,5,6,7,8,9,10],
    'emp_name':['John','Smith','David','Sam','Peter','Mary','Jane','Tom','Jerry','Lucy'],
    'emp_salary':[50000,60000,55000,70000,65000,80000,75000,72000,68000,62000],
    'emp_department':['IT','HR','Finance','IT','HR','Finance','IT','HR','Finance','IT'] ,
    'join_date':['2020-01-15','2019-03-20','2021-07-10','2018-11-05','2020-06-25','2019-09-30','2021-02-18','2018-12-12','2020-08-22','2019-05-14'] 
}
df=pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(3))
print(df.info())