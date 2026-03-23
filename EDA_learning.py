import pandas as pd 

import matplotlib.pyplot as plt

Data = {
      
    "Name" : ["A","B","C","D","E","F"],
    "Hours_Studied": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 40, 50, 60, 70, 80],
}

df = pd.DataFrame(Data)

df.head()
print(df.head())

df.tail()
print(df.tail())

df.shape
print(df.shape)

df.info()
print(df.info())

df.describe()
print(df.describe())

df.columns
print(df.columns)

df.isnull().sum()
print(df.isnull().sum())

plt.hist(df["Marks"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Students Marks")
plt.show()

plt.plot(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours_studied")
plt.ylabel("Marks")
plt.title("Students Mark Analaysis")
plt.show()

plt.scatter(df["Hours_Studied"],df["Marks"])
plt.xlabel("Hours_Studies")
plt.ylabel("Marks")
plt.title("Scatter Plot Graph")
plt.show()

plt.boxplot(df["Marks"])
plt.ylabel("Marks")
plt.title("Relationship between study hours & Marks")
plt.show()

results={}

results["hours_ greater_than_4"] = df[df["Hours_Studied"] > 4]

results["Marks_greater_than_55"] = df[df["Marks"] > 55]

results["hours_less_than_4_and_marks_greater_than_60"] = df[(df["Hours_Studied"] < 4) & (df["Marks"] > 60)]

results["Abdur"] = df[(df["Hours_Studied"] > 2) & (df["Marks"] > 50) ]

results["abdu"] = df[(df["Hours_Studied"] > 5) & (df["Marks"] > 70) ]

results["query_filter"] = df.query( "Hours_Studied > 5 and Marks > 70")

results["sort_values"] = df.sort_values(by="Name" , ascending=False)


print(results)