"""import pandas as pd 
data = {
    "marks" :[80,70,90,70,60]

}
df= pd.DataFrame(data)
print("Mean", df["marks"].mean())
print("Median", df["marks"].median())
print("Mode", df["marks"].mode()[0])"""
"""import pandas as pd
data = {
    "Old_name" :[1,2,3]

}
df= pd.DataFrame(data)
df.rename(columns={"Old_name":"New_name"}, inplace=True)
print(df)"""
"""import pandas as pd
data = {
    "Marks": [90,None,80,70]
}
df=pd.DataFrame(data)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print(df)"""
"""import pandas as pd
df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["a","b","c"]
})
df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[90,80,70]
})
merged_df = pd.merge(df1, df2, on="ID")
print(merged_df)""""""
import pandas as pd
data = {
    "City":["Chennai","Madurai","Chennai"]
}
df = pd.DataFrame(data)
print(df["City"].value_counts())"""
"""import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Marks":[90,80,70,60,50]
}
df = pd.DataFrame(data)
plt.hist(df["Marks"])
plt.title("Marks Distribution   ")
plt.show()"""
"""import pandas as pd
import matplotlib.pyplot as plt
data={
    "Marks":[90,80,70,60,50]}
df=    pd.DataFrame(data)
plt.boxplot(df["Marks"])
plt.show()"""
"""import pandas as pd
data = {   
    "Marks":[90,80,70,60,50]
}
df = pd.DataFrame(data)
df["Result"] = df['Marks'].apply(lambda x: "Pass" if x >=50 else "Fail")
print(df)"""
"""import pandas as pd
data= {
    "Name":["john","sam"]
}
df = pd.DataFrame(data)
df["Upper"]= df["Name"].str.upper()
print(df)"""
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Sales":[100,150,200,250,300],
    "profit":[20,30,40,50,60]
}
df = pd.DataFrame(data)
plt.scatter(df["Sales"], df["profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()