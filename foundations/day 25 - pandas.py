import pandas as pd
nums = [34, 55, 66, 77]
new = pd.Series(nums, index = [1, 2, 3, 4])
#print(new)

fruits = ["apple", "orange", "banana"]
new_2 = pd.Series(fruits, index=[1, 5, 6])
#print(new_2)

#making dictionaries

random_dct = {"Name":"Elliot","Age":43,"Job":"Firefigher"}
new_dct = pd.Series(random_dct)
#print(new_dct)

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

df = pd.DataFrame(data, columns = ["Array1","Array2","Array3"])
print(df)

#df with dictionary
dct = {
    "names":["Boy", "Girl", "Tom"], 
    "ages":[24, 55, 66],
    "city":["Rome", "Paris", "Berlin"]
}
dct_df = pd.DataFrame(dct)
#adding a new column
friends = ["Milo", "Josh", "Brandon"]
dct_df["bestie"] = friends #key is a column
print(dct_df)
print(dct_df.bestie.dtype)