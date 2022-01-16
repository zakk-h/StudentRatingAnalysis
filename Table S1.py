import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

# your file path
src = r"Dataset from RateMyProfessor.com for professors' teaching evaluation.csv"
df = pd.read_csv(src)

# Yearly distribution
df["years"] = pd.DatetimeIndex(df['Post_date']).year
record_year = df["years"].value_counts().sort_index()
prof_year = df.drop_duplicates(['Professor_ID', 'School_name', 'Department_ID',"years"])["years"].value_counts()
year_dist = pd.concat([prof_year,record_year],axis=1).reset_index().astype(int)
year_dist.columns = [ "Year","Professor","Evaluation record"]
year_dist.to_excel("years.xlsx")

# To indentify the country locations, we first extracted the geolocation code of the affiliations
# by the following code block and then manually linked them to countries.
'''
def find_location(x):
    geolocator = Nominatim(user_agent="my-application")
    location = geolocator.geocode(x)
    if location:
        address = location.address
        address_list = address.split(", ")
        return address_list[-1]
    else:
        return "not found"

try:
    prof_state = df["State_name"].str.strip().value_counts().reset_index()
    prof_state["country"]=prof_state["index"].apply(find_location)
except:
    print("error")
prof_state.to_excel(r"prof_state.xlsx")
'''
# after the linkage of country information, we get a new spreadsheet
df_prof_state = pd.read_excel(r"prof_state.xlsx")
df["State_name"] = df["State_name"].str.strip()
df2 = pd.merge(df, df_prof_state[["State_name","country"]], on = "State_name", how = "left")
record_country = df2["country"].value_counts().sort_index()
prof_country = df2.drop_duplicates(['Professor_ID', 'School_name', 'Department_ID',"country"])["country"].value_counts()
country_dist = pd.concat([prof_country,record_country],axis=1).reset_index()
country_dist.columns = ["Country","Professor","Evaluation record"]
country_dist.to_excel("country.xlsx")
