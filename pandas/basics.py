import pandas as pd

#pd.show_versions()
#s = pd.Series(["IND","NZ","ENG","AUS"])
#print(s)

#dataframe 

employee_id = {
    "ID": ["101","102","103","104"],
    "Name" : ["Shaan","Ravi","Kiran","Varun"],
    "City" : ["Bangalore","Hyderabad","Pune","Surat"]
}
table = pd.DataFrame(employee_id)
print(table)