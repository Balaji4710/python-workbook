"""import pandas as pd
data = pd.read_csv("C:\\Users\\Home\\OneDrive\\Documents\\work.csv")
print(data)"""
"""import pandas as pd
data = {
    "Name": ["Arun","Priya"],
    "Marks":[85,90]

}
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
print("CSV File created Successfully")"""
"""import pandas as pd
data = pd.read_csv("output.csv")
print("First 5 rows of the data:")
print(data.head())
print("\nAverage Marks:") 
print(data["Marks"].mean())
print("Highest Marks:")
print(data["Marks"].max())"""
"""import pandas as pd
data = pd.read_csv("C:\\Users\\Home\\OneDrive\\Documents\\students.csv")
print("original data")
print("data")
data = data.drop_duplicates()
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Marks"] = data["Marks"].fillna(0)
data["Name"] = data["Name"].str.strip()
print("Cleaned Data:")
print(data)"""
"""import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Home\\Downloads\\students.csv")
names = data["Name"]
marks = data["Marks"]
plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()"""
"""import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Home\\Downloads\\students.csv")
plt.plot(data['Name'],data['Marks'])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()"""
"""import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Home\\Downloads\\students.csv")
plt.pie(
    data["Marks"],
    labels = data["Name"],
    autopct = "%1.1f%%"

)
plt.title("Marks Percentage")
plt.show()"""
"""import pandas as pd
data = pd.read_csv("C:\\Users\\Home\\Downloads\\students.csv")
print("Original Data:")
print(data)
filtered_data = data[data["Marks"] > 80]
print("Filtered Data (Marks > 80):")
print(filtered_data)"""
""""import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Home\\Downloads\\students.csv")
data["Total"] = data["Maths"] + data["Science"] + data["English"]
data["Average"] = data["Total"] / 3
print("\n Student perfomance:")
print(data)
topper = data.loc[data["Average"].idxmax()]
print("\n Topper:")
print(topper)
plt.bar(data["Name"],data["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.show()"""
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet"],
    "Region": ["North","South","East","West","North","South"],
    "Sales": [50000,30000,20000,45000,35000,25000],
    "Cost": [30000,20000,12000,28000,22000,15000],
    "Quantity": [5,10,8,4,7,6]
}
df = pd.DataFrame(data)
print("-------Dataset-------")
print(df)
df["Profit"] = df["Sales"] - df["Cost"]
print("\n-------Profit analysis-------")
print(df[["Product","Sales","Cost","Profit"]])
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print(f"\nTotal Sales: {total_sales}")
print(f"Total Profit: {total_profit}")
print("\n-------Sales by Product-------")
productsales = df.groupby("Product")["Sales"].sum()
print(productsales)
region_profit = df.groupby("Region")["Profit"].sum()
print("\n-------Profit by Region-------")
print(region_profit)
top_product = productsales.idxmax()
print(f"\nTop Selling Product: {top_product}")
average_sales = df["Sales"].mean()
high_profit = df[df["Profit"] > 10000]
print("\n-------High Profit Transactions-------")
print(high_profit)
plt.bar(productsales.index, productsales.values)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product")
plt.show()
plt.pie(region_profit.values, labels=region_profit.index, autopct="%1.1f%%")
plt.title("Region-wise Profit Distribution")
plt.show()
plt.plot(df['Sales'],marker='o')
plt.xlabel("Transaction")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()
print("total sales",total_sales)
print("total profit",total_profit)
print("top product",top_product)
print("average sales",average_sales)
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
print("\n-------Profit Margin Analysis-------")
print(df[["Product","Profit Margin"]])
df['Customer_Type'] = df['Quantity'].apply(lambda x: 'Bulk Buyer' if x > 7 else 'Regular Buyer')
print("------Customer Type ------")
print(df[['Product','Quantity','Customer_Type']])
print(df)