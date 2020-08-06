import pandas


# df = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
# print(df)
# print("----------------------------------------------------------------------------")
# print()

df = pandas.read_json("http://pythonhow.com/supermarkets.json")
print(df)

print(df.loc[:,"Country"])
print("----------------------------------------------------")
print(df.iloc[3,1:4])
print("------------------------------------------------------")
print(df.loc[:,"State"])
print("--------------------------------------------------------")
print(df.iloc[4,0:7])
