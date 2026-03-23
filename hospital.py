import pandas as pd 
df =pd.read_csv(r"C:\Users\abdur\OneDrive\Documents\Desktop\python\hospital_patient_data_with_doctor_names.csv")
print(df)

df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()


df = df.sort_values(by="Patient_ID")
df['Patient_Name'] = df['Patient_Name'].fillna("Unknown")
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Gender'] = df['Gender'].fillna("Unknown")
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Day'] = df['Admission_Date'].dt.day_name()
df['Department'] = df['Department'].fillna("General")
df["Doctor_ID"] = df['Doctor_ID'].fillna(0)
df['Doctor_Name'] = df['Doctor_Name'].fillna("General Doctor")
df['Wait_Time_Minutes'] = df['Wait_Time_Minutes'].fillna(df['Wait_Time_Minutes'].mean())
df['Billing_Amount'] = df['Billing_Amount'].fillna(df['Billing_Amount'].mean())


from sqlalchemy import create_engine
username = "root",
password = "root",
host = "localhost",
port = "3305",
database = "hospital"


engine = create_engine(f"mysql+pymysql://root:root@localhost:3305/hospital")
table_name = "hospital_records"
df.to_sql(table_name, engine, if_exists='append', index=False)


