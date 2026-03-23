import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [35, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

# # Line plot
# plt.plot(df['Hours_Studied'], df['Marks'])
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Study Hours vs Marks")
# plt.show()

# # scatter plot
# plt.scatter(df['Hours_Studied'], df['Marks'])
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Relationship between study hours and marks ")
# plt.show()

# # box plot
# plt.boxplot(df['Marks1'])
# plt.ylabel("Marks")
# plt.title("Marks Distribution")
# plt.show()

results = {}
results["hours_gt_4"] = df[df["Hours_Studied"] > 4]

results["marks_gt_60"] = df[df["Marks"] > 60]

results['hours_gt_3_and_marks_gt_60'] = df[
    (df["Hours_Studied"] > 3) & (df['Marks'] >= 60) ]

results['hours_lt_3_or_marks_gt_80'] = df[
    (df["Hours_Studied"] < 3) & (df['Marks'] > 80) ]

results['query_filter'] = df.query(
    "Hours_Studied >= 5 and Marks >=70"
)

results['sorted_marks_desc'] = df.sort_values(
    by='Marks', ascending=False
)

results['name_and_marks'] = df[['Name']]

print(results)

