"""import pandas as pd
data ={
    "product": [ "A","A","B","B"],
    "Month": ["jan","feb","Jan","feb"],
    "sales": [100,200,300,400]
}
df = pd.DataFrame(data)
pivot= df.pivot_table(values="sales", index="product", columns="Month", aggfunc="sum")
print(pivot)
"""
"""import pandas as pd
data ={
    "Marks": [100,200,300,400],
}
df = pd.DataFrame(data)
df["Percentage"] = (df["Marks"]/100)*100
print(df)"""
"""import pandas as pd
data ={
   "Marks": [89,87,67,70]

}
df = pd.DataFrame(data)
df['Rank'] = df["Marks"].rank(ascending=False)
print(df)"""
"""import pandas as pd
data ={
    "Result": ["P","F","P","F"],
}
df = pd.DataFrame(data)
df["Result"] = df["Result"].map({"P": "Pass", "F": "Fail"})
print(df)"""
"""import pandas as pd
data ={
    "Name" : ["John","Alexander"]
}
df = pd.DataFrame(data)
df["Length"] = df["Name"].str.len()
print(df)"""
"""import pandas as pd
data ={
    "sales":[1000,5000,2000]

}
df= pd.DataFrame(data)
df["Status"] = df["sales"].apply(lambda x: "High" if x > 3000 else "Low")
print(df)"""
"""import pandas as pd
data ={
    "Marks": [80,90]
}
df = pd.DataFrame(data)
df = df.reset_index()
print(df)"""
"""import pandas as pd
data ={
    "Value": [10,20,30,40,50]

}
df = pd.DataFrame(data)
print(df.sample(2))"""
"""import pandas as pd
import matplotlib.pyplot as plt
data ={
    "Sales": [100,200,300],
    "Profit": [20,40,60]
}
df = pd.DataFrame(data)
corr = df.corr()
plt.imshow(corr)
plt.colorbar()
plt.show()"""
"""import pandas as pd
data ={
    "Customer": ["A","B","A","C","A"]


}
df = pd.DataFrame(data)
retention = df["Customer"].value_counts()
print(retention)"""
"""import pandas as pd
data ={
   "order_value": [1000,2000,1500]
}
df = pd.DataFrame(data)
aov = df["order_value"].mean()
print("Average Order Value:", aov) """
"""import pandas as pd
data ={
    "Product": ["A","B","C"],
    "Sales": [500,900,700]
}
df = pd.DataFrame(data)
df["Rank"] = df["Sales"].rank(ascending = False)
print(df)"""
"""import pandas as pd
data ={
    "Day": ["Mon","tue","Wed"],
    "Visitors": [100,150,200]
}
df = pd.DataFrame(data)
print("Total Visitors:", df["Visitors"].sum())"""
import pandas as pd
data = {
    "Expected":[5000,7000],
    "Actual":[4500,6500]
}
df = pd.DataFrame(data)
df["Loss"] = df["Expected"] - df["Actual"]
print(df)