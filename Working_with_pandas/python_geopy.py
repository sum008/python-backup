import pandas
from geopy.geocoders import Nominatim

df = pandas.read_json("supermarkets.json")
print(df)
nom = Nominatim(scheme="http")
# print(nom.geocode("Nyay-Khand-2,Indirapuram, Ghaziabad ,201014"))

df["Address"] = df["Address"] +" , "+df["City"]+" , "+df["State"]+" , "+df["Country"]
print(df["Address"])

df["Coordinates"]=df["Address"].apply(nom.geocode)

print(df)